import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
url = 'https://store.steampowered.com/specials#tab=TopSellers'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

new_realises = soup.find('div', attrs={'id':'NewReleasesRows'})
newRealiseContents = soup.findAll('a', attrs={'class':'tab_item'})

for newRealiseContent in newRealiseContents:
    imgUrl = newRealiseContent.find('img', attrs={'class':'tab_item_cap_img'})['src']
    titles = newRealiseContent.find('div', attrs={'class':'tab_item_name'}).text
    response = requests.get(imgUrl, headers=headers, stream=True)
    fileName = imgUrl.split("/")[-1].split("?")[0]
    ext = fileName[-4:]
    if response.ok:
        with open('images/'+ re.sub(r'(?u)[^-\w.]', '_', titles)+ ext, 'wb') as a:
            a.write(response.content)


