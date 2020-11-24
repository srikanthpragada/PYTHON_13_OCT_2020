import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com/rss.xml"
resp = requests.get(URL)
if resp.status_code != 200:
    print(f'Sorry! Could not get details for {URL}')
    exit(0)

bs = BeautifulSoup(resp.text, 'lxml-xml')

for item in bs.find_all("item"):
    print(item.title.text.strip())
    print(item.link.text.strip())
    print('-' * 80)

