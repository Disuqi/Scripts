from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

def showMe(something):
    url = 'https://www.pexels.com/'
    driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
    driver.get(url)
    box = driver.find_element_by_xpath('/html/body/header/section/div/form/div[1]/input')
    box.send_keys(something)
    box.send_keys(Keys.ENTER)
    last_height = driver.execute_script('return document.body.scrollHeight')
    scrolls=0
    while True:
        scrolls+=1
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height
        if scrolls == 20:
            break


    items=[]
    for i in range(1, 100):
        try:
            for x in range(1, 3):
                items.append(driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[6]/div[1]/div['+str(x)+']/div['+str(i)+']/article/a[1]/img').get_attribute('src'))
        except:
            pass
    return items


print(showMe('camel'))