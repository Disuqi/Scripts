from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

def showMe():
    url = 'https://na.leagueoflegends.com/en-us/champions/'
    driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
    driver.get(url)
    last_height = driver.execute_script('return document.body.scrollHeight')
    scrolls=0
    while True:
        scrolls+=1
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height
        if scrolls == 20:
            break


    items=[]
    for i in range(1, 200):
        try:
            champ = str(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/section/div[2]/section[2]/div[2]/a['+ str(i)+']/span[2]/span').text.lower())
            champName = champ[0].upper() + champ[1:].lower()
            items.append(champName)
        except:
            pass
    return items


print(showMe())