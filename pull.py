import requests
import random
import subprocess
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

parser = 'html.parser'

def get_maxn_comics():
    site = requests.get(f'https://xkcd.com/').text
    s = bs(site, parser)
    a = s.find_all('a')
    url = a[26].text
    maxn = int(urlparse(url).path.strip('/'))

    return maxn

maxn = get_maxn_comics()
comicn = random.randint(1, maxn)
data = {}
text = requests.get(f'https://xkcd.com/{comicn}').text
s = bs(text, parser)

for tag in s.find_all('div', id="middleContainer"):
    data['title'] = tag.find('div', id='ctitle').text
    data['url'] = tag.find_all('a')[-1]['href']
    print(tag.find_all('a')[-2]['href'])

print(f"comic found: {data['title']} (#{comicn})")
subprocess.run(['wget', data['url'], '-q'])
