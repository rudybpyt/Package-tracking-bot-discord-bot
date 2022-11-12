from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import os

def getTrackingDetails(trackingNumber):
    opts = Options()
    opts.headless = True  # Uncomment if the headless version needed
    opts.binary_location = "<PATH TO GOOGLE CHROME>"
    chrome_driver = "<PROJECT PATH>/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)

    temp = []
    temp2 = []
    driver.get(f'https://track24.net/service/tracking/tracking/{trackingNumber}')
    soup = BeautifulSoup(driver.page_source)

    divs = soup.findAll(class_='trackingInfoRow')
    for div in divs:
        date = div.find(class_='date').get_text()
        time = div.find(class_='time muted').get_text()
        info = div.find(class_='trackingInfoDetails').get_text()
        print(date + " : "+time +' '+ info)
        temp2 = [date,time,info]
        temp.append(temp2)
        pd.DataFrame(temp).to_csv(f'{trackingNumber}.csv')

def checkForUpdates(trackingNumber):
    opts = Options()
    opts.headless = True  # Uncomment if the headless version needed
    opts.binary_location = "<PATH TO GOOGLE CHROME>"
    chrome_driver = "<PROJECT PATH>/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)

    df = pd.read_csv(f'{trackingNumber}.csv')
    driver.get(f'https://track24.net/service/tracking/tracking/{trackingNumber}')
    soup = BeautifulSoup(driver.page_source)
    temp2 = []
    temp = []
    df2 = pd.DataFrame()
    divs = soup.findAll(class_='trackingInfoRow')
    for div in divs:
        date = div.find(class_='date').get_text()
        time = div.find(class_='time muted').get_text()
        info = div.find(class_='trackingInfoDetails').get_text()
        print(date + " : " + time + ' ' + info)
        temp2 = [date, time, info]
        temp.append(temp2)
        pd.DataFrame(temp).to_csv(f'temp.csv')