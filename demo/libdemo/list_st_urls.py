import requests
from bs4 import BeautifulSoup

domain = "http://www.srikanthtechnologies.com"
resp = requests.get(domain)
if resp.status_code != 200:
    print('Sorry! Could not get details of srikanthtechnologies.com!')
    exit(0)

bs = BeautifulSoup(resp.text, 'html.parser')

for tag in bs.find_all('a'):
    if 'href' in tag.attrs:
        value = tag['href']
        if len(value) > 1:
            pos = value.find('?')
            if pos > 0:
                value = value[:pos]
            if value.startswith("http"):
                print(value)
            else:
                print(domain + "/" + value)
