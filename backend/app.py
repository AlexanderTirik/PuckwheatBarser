import asyncio

import aiohttp
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from bs4 import BeautifulSoup as bs
from itertools import chain


app = Sanic(__name__)
CORS(app)
sem = None


@app.listener('before_server_start')
def init(sanic, loop):
    global sem
    concurrency_per_worker = 4
    sem = asyncio.Semaphore(concurrency_per_worker, loop=loop)


async def bounded_fetch(session, url):
    """
    Use session object to perform 'get' request on url
    """
    async with sem, session.get(url) as response:     
        return await response.text()


async def get_soup(url):
    """
    Download html from site
    """
    async with aiohttp.ClientSession() as session:
        response = await bounded_fetch(session, url)
        return bs(response, features="html.parser")


def parse_weight(weight):
    """
    Parse the numerical value of the weight from a string
    """
    if weight.endswith('кг'):
        return 1000*int(weight[:-2])
    else:
        if weight.count('*'):
            number, _, weight_one = weight.partition('*')
            return int(number)*parse_weight(weight_one)
        else:
            return int(weight[:-1])


def clean_weight(weight):
    weight_value = parse_weight(weight)
    if weight_value % 1000 == 0:
        weight = str(int(weight_value / 1000)) + 'кг'
    weight = ''.join(weight.split())
    return weight


async def parse_fozzy():
    """
    Parse buckwheat from fozzy
    """
    url = 'https://fozzyshop.ua/300143-krupa-grechnevaya'
    shop = 'Fozzy'

    soup = await get_soup(url)
    products = soup.find_all('div', class_='js-product-miniature-wrapper')
    
    data = []
    for product in products:
        try:
            description = product.find('div', class_='product-description')
            
            price = description.find('span', class_='product-price').get('content')
            name = description.find('div', class_='h3 product-title').a.get_text()
            source = description.find('div', class_='product-brand').a.get_text()
            productUrl = description.find('div', class_='h3 product-title').a.get('href')
            imgUrl = product.find('div', class_='thumbnail-container').a.img.get('src')
            weight = product.find('div', class_='product-reference text-muted').a.get_text().replace('Фасовка: ', '').strip()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)

            data.append({
                'price': price,     
                'name': name,
                'source': source,
                'productUrl': productUrl,
                'imgUrl': imgUrl,
                'shop': shop,
                'weight': weight,
                'weightValue': weight_value
            })
        except Exception as e:
            print(f'Something was wrong: {e}')
    
    return data


async def parse_epicentrk():
    """
    Parse buckwheat from epicentrk
    """
    url = 'https://epicentrk.ua/ua/shop/krupy-i-makaronnye-izdeliya/fs/vid-krupa-grechnevaya/'
    host = 'https://epicentrk.ua'
    shop = 'Епіцентр'

    soup = await get_soup(url)
    products = soup.find_all('div', class_='card-wrapper')

    data = []
    for product in products:
        try:
            name = product.find('div', class_='card__name').a.b.get_text().strip()
            price = product.find('span', class_='card__price-sum').contents[0].strip()
            source = product.find('ul', class_='card__characteristics').find_all('li')[1].get_text().replace('Бренд:', '').strip()
            productUrl = host + product.find('a', class_='card__photo').get('href') 
            imgUrl = product.find('a', class_='card__photo').img.get('src')
            weight = product.find('ul', class_='card__characteristics').find_all('li')[2].get_text().replace('Вага:', '').strip()
            weight = clean_weight(weight)         
            weight_value = parse_weight(weight)

            data.append({
                'name': name,
                'price': price,
                'source': source,
                'productUrl': productUrl,
                'imgUrl': imgUrl,
                'weight': weight,
                'weightValue': weight_value
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data


@app.route("/")
async def index(request):
    return json({"api": "v1"})


@app.route("get_data")
async def get_data(request):
    data_fozzy = await parse_fozzy()
    data_epicentrik = await parse_epicentrk()
    # next calls of parsers
    
    data = list(chain(data_fozzy, data_epicentrik))
    return json(data)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        auto_reload=True
    )
