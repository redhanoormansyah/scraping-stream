from uu import encode
import requests
from bs4 import BeautifulSoup
import csv

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
url = 'https://store.steampowered.com/specials#p=0&tab=NewReleases'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text,"html.parser")

new_realises = soup.findAll('a', attrs={'class': 'tab_item'})
file = open('steam.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Price', 'Tags'])

for new_realise in new_realises:
    if(new_realise.find('div', attrs={'class':'tab_item_name'}) !=None):
        title = new_realise.find('div', attrs={'class':'tab_item_name'}).text
    else:
        title = ''

    if (new_realise.find('div', attrs={'class': 'discount_final_price'}) != None):
        price = new_realise.find('div', attrs={'class': 'discount_final_price'}).text
    else:
        price = ''
    if (new_realise.find('div', attrs={'class': 'tab_item_top_tags'}) != None):
        tags = new_realise.find('div', attrs={'class': 'tab_item_top_tags'}).text
    else:
        tags = ''

    file = open('steam.csv','a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, price, tags])
    file.close()
