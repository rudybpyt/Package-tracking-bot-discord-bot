import discord
from discord.ext import tasks
from datetime import datetime as dt
import pandas as pd
import json
import parse1

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tracking_numbers = []

with open('channelid.txt', 'r') as f:
    cid = int(f.read())
with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
     print('Prefix: ' + c['prefix'])
     print('Token: ' + c['token'])

@client.event
async def on_ready():
    print(f"logged on as {client.user}")
    checkForUpdates.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(f'{c["prefix"]}test'):
        await message.channel.send(f"test!")
    if message.content.startswith(f'{c["prefix"]}track'):
        txt = message.content
        msg = txt.split(" ")
        parse1.getTrackingDetails(msg[1])
        tracking_numbers.append([msg[1],msg[2]])
        await message.channel.send(f"Tracking package {msg[2]}...")
        df = pd.read_csv(f'{msg[1]}.csv')
        for i in range(len(df)):
            await message.channel.send(f"{df.iloc[i,1]}:{df.iloc[i,2]}-{df.iloc[i,3]}")
    if message.content.startswith(f'{c["prefix"]}here'):
        channelid = message.channel.id
        print(channelid)
        with open('channelid.txt', 'w') as f:
            f.write(str(channelid))
        await message.channel.send(f"I will announce updates in this channel now")

#check for updates every hour
@tasks.loop(hours=1)
async def checkForUpdates():
    BotChannel = client.get_channel(cid)
    print("looking for updates to tracking data")
    index = -1
    for x in tracking_numbers:
        index += 1
        parse1.checkForUpdates(tracking_numbers[index][0])
        df1 = pd.read_csv(f'{tracking_numbers[index][0]}.csv')
        df2 = pd.read_csv('temp.csv')
        temp = df1.compare(df2)
        if temp.empty != True:
            await BotChannel.send(f"update for package:{tracking_numbers[index][1]}")
            for i in range(len(temp)):
                print(f"{temp.iloc[i, 1]}:{temp.iloc[i, 2]}-{temp.iloc[i, 3]}")

client.run(c['token'])