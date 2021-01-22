import aiohttp
from bs4 import BeautifulSoup as bs


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
    weight_value = parse_weight(weight)
    if weight_value % 1000 == 0:
        weight = str(int(weight_value / 1000)) + 'кг'
    weight = ''.join(weight.split())
    return weight
