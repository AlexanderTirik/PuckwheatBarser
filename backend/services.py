import aiohttp
from bs4 import BeautifulSoup as bs
import re
from time import time


async def bounded_fetch(session, url):
    """
    Use session object to perform 'get' request on url
    """
    async with session.get(url) as response:
        return await response.text()


async def get_response(url):
    """
    Download response from site
    """
    async with aiohttp.ClientSession() as session:
        response = await bounded_fetch(session, url)
        return response


def get_soup(response):
    return bs(response, features="html.parser")


def parse_weight(weight):
    """
    Parse the numerical value of the weight from a string
    """
    if weight.endswith('кг'):
        return 1000 * int(weight[:-2])
    else:
        if weight.count('x'):
            number, _, weight_one = weight.partition('x')
            return int(number) * parse_weight(weight_one)
        else:
            return int(weight[:-1])


def clean_weight(weight):
    """
    Parse weight and transform to pretty and format uniformly
    """
    weight_pattern = r'[0-9]+.*'
    weight = re.search(weight_pattern, weight).group(0)
    if 'кг' in weight:
        weight = weight.replace('кг', '').strip() + ' ' + 'кг'
    else:
        weight = weight.replace('г', '').strip() + ' ' + 'г'
    weight = weight.replace('*', 'x')

    weight_value = parse_weight(weight)
    if weight_value % 1000 == 0:
        weight = str(int(weight_value / 1000)) + ' кг'
    return weight
    

def clean_name(name):
    """
    Parse clean name, exclude weight and unnecessary words
    """
    skip_pattern = r'(\([0-9]*\))|(([0-9]+[\*х])?[0-9]+\s?к?г)|([0-9]+\S+)|(\.)|(\")'
    name = re.sub(skip_pattern, '', name)
    name = name.strip()
    return name


def parse_source_from_name(name):
    """
    Parse source from name of buckwheat
    Recommended for use with data from Auchan
    """
    skip_words = [
        'крупа', 'гречана', 'ядриця', 'швидкорозварювана', 'в', 'пакетиках', 'пропарена', 'органічна',
        'швидкорозварювальна', 'зелена', 'непропарена', 'несмажена', 'гречана', 'з', 'грибами', 'україна',
        'гречка'
    ]
    lst = name.split()
    lst = map(lambda el: el if not el.lower() in skip_words else '', lst)
    source = ' '.join(lst).strip()
    return source


def fixed_price_format(price, digits=2):
    return f'{float(price):.{digits}f}'


def check_is_packed(source, default_source=None):
    if source:
        return True, source
    else:
        return False, default_source