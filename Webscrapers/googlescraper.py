from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

def showMe(something):
    url = 'https://images.google.co.uk/'
    driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/span/div/div/div[3]/button[2]').click()
    box = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/input')
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
        if scrolls == 10:
            break
    items=[]
    for i in range(1, 100):
        try:
            driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[4]/div[1]/div/div/div/div/div[1]/span/div[1]/div[1]/div['+str(i)+']/a[1]/div[1]/img').click()
            time.sleep(2)
            items.append(driver.find_element_by_class_name('n3VNCb').get_attribute("src"))
        except:
            print('exception')
    return items


print(showMe('people from bangladesh'))