# Package tracking bot (discord bot)
A bot to give you updates on a package from a given tracking number. After intially tracking the package, the bot will announce any updates to the package to the channel afterwards. 

## Setup
Edit the config.json file and chose your desired prefix for commands as well as inserting your token.
Using the (prefix)here command to set the bot to announce the reminders in your desired channel.

Edit parse1.py and put in the directory to chrome as well as the path to the chromedriver.exe
(chromedriver.exe can be downloaded from https://sites.google.com/chromium.org/driver/downloads/)

## Commands
### (prefix)test:
test if the bot is alive and responding, bot should reply with "I am alive"
### (prefix)track:
Ask the bot to track a package, format should be (prefix)track (tracking number) (name of package)
example of this: $track ZW924750388GB test
### (prefix)here
Set this channel for the bot to announce updates to your package
