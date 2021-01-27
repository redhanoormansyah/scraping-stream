
import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template



app = Flask(__name__)
@app.route('/')
def top_sellers():


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    url = 'https://store.steampowered.com/specials#tab=TopSellers'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    # steams = soup.findAll('div',attrs={'class':'carousel_items'})
    top_sellers = soup.findAll('a', attrs={'class': 'tab_item'})
    return render_template('grid_template.html', top_sellers=top_sellers)




if __name__ == '__main__':
    app.run(debug=True)

# 
# for topSeller in top_sellers:
#     print('Titles: ', topSeller.find('div', attrs={'class':'tab_item_name'}).text)
#     print('Images: ', topSeller.find('div', attrs={'class':'tab_item_cap'}).find('img'))
#     print('Tags: ', topSeller.find('div', attrs={'class':'tab_item_top_tags'}).text)
