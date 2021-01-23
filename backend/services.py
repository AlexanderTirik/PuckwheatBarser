import aiohttp
from bs4 import BeautifulSoup as bs
import re


async def bounded_fetch(session, url):
    """
    Use session object to perform 'get' request on url
    """
    async with session.get(url) as response:
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
        return 1000 * int(weight[:-2])
    else:
        if weight.count('*'):
            number, _, weight_one = weight.partition('*')
            return int(number) * parse_weight(weight_one)
        else:
            return int(weight[:-1])


def clean_weight(weight):
    """
    Parse weight and transform to pretty and format uniformly
    """
    weight_value = parse_weight(weight)
    if weight_value % 1000 == 0:
        weight = str(int(weight_value / 1000)) + 'кг'
    weight = ''.join(weight.split())
    return weight


def clean_name(name):
    """
    Parse clean name, exclude weight and unnecessary words
    """
    weight_pattern = r'(\([0-9]*\))|(([0-9]+[\*х])?[0-9]+\s?к?г)|([0-9]+\S+)|(\.)|(\")'
    name = re.sub(weight_pattern, '', name)
    name = name.strip()
    return name


def parse_source_from_name(name):
    """
    Parse source from name of buckwheat
    """
    # to do
    return "-"


def fixed_price_format(price, digits=2):
    return f'{float(price):.{digits}f}'
