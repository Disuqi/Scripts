import requests

url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

open('C:/Users/Disuqi/Downloads/facevook.ico', 'wb').write(r.content)