import pandas as pd
from selenium import webdriver
from requests_html import HTMLSession


session = HTMLSession()

url = 'https://www.tase.co.il/en/market_data/security/662577/major_data'
r = session.get(url)
r.html.render(sleep = 2)
result = r.html.xpath('//*[@id="moreCollapse"]/div[2]/div/div[4]/div[2]/b', first = True).text
secondUrl = 'https://www.tase.co.il' + r.html.xpath('//*[@id="mainContent"]/security-lobby/security-major/section[1]/div/div[1]/div/div[3]/div/div[1]/div/div/a', first = True).attrs['href']
r = session.get(secondUrl)
r.html.render(sleep = 2)
perc = r.html.xpath('//*[@id="mainContent"]/company-lobby/ng-component/company-details/section/div/company-info/div[2]/div[2]/div[2]/div/div[2]/div[2]/b', first = True).text

excelFile = pd.DataFrame({
    'Capital Lister for Trading' : [result],
    'Change' : [perc]
})
excelFile.to_excel('something.xlsx')


# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=options)
# browser.get(url)
# print(browser.find_element_by_class_name('bond_rate_num'))
# browser.quit()

# period_names = [item.find(class_='period-name').get_text() for item in items]
# short_desc = [item.find(class_='short-desc').get_text() for item in items]
# temp = [item.find(class_='temp').get_text() for item in items]


# print(weather_stuff)

# weather_stuff.to_excel('weatherwebscraper.xlsx')