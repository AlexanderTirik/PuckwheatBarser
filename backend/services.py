import re

import aiohttp
from bs4 import BeautifulSoup as bs


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
    if weight.endswith("кг"):
        return 1000 * int(weight[:-2])
    else:
        if weight.count("x"):
            number, _, weight_one = weight.partition("x")
            return int(number) * parse_weight(weight_one)
        else:
            return int(weight[:-1])


def clean_weight(weight):
    """
    Parse weight and transform to pretty and format uniformly
    """
    weight_pattern = r"[0-9]+.*"
    weight = re.search(weight_pattern, weight).group(0)
    if "кг" in weight:
        weight = weight.replace("кг", "").strip() + " " + "кг"
    else:
        weight = weight.replace("г", "").strip() + " " + "г"
    weight = weight.replace("*", "x")

    weight_value = parse_weight(weight)
    if weight_value % 1000 == 0:
        weight = str(int(weight_value / 1000)) + " кг"
    return weight


def clean_name(name):
    """
    Parse clean name, exclude weight and unnecessary words
    """
    skip_pattern = r"(\([0-9]*\))|(([0-9]+[\*х])?[0-9]+\s?к?г)|([0-9]+\S+)|(\.)|(\")"
    name = re.sub(skip_pattern, "", name)
    name = name.strip()
    return name


def parse_source_from_name(name, default_name=None):
    """
    Parse source from name of buckwheat
    Recommended for use with data from Auchan
    """
    skip_words = [
        "крупа",
        "гречана",
        "ядриця",
        "швидкорозварювана",
        "в",
        "пакетиках",
        "пропарена",
        "органічна",
        "швидкорозварювальна",
        "зелена",
        "непропарена",
        "несмажена",
        "гречана",
        "з",
        "грибами",
        "україна",
        "гречка",
    ]
    lst = name.split()
    lst = map(lambda el: el if not el.lower() in skip_words else "", lst)
    source = " ".join(lst).strip()

    return source or default_name


def fixed_price_format(price, digits=2):
    """
    Set a fixed number of decimal places
    """
    return f"{float(price):.{digits}f}"


def asc_sort_by_price(data):
    """
    Sorts products by price in ascending order
    """
    return sorted(data, key=lambda el: float(el.get("price")))


def sort_by_price(data, order="NONE"):
    """
    Sorts products by price
    """
    if order == "NONE":
        return data
    elif order == "ASC":
        return asc_sort_by_price(data)
    elif order == "DESC":
        return list(reversed(asc_sort_by_price(data)))


def is_buckwheat(name):
    """
    Check the product is buckwheat
    """
    good = ["гречка", "гречана", "крупа"]
    bad = [
        "борошно",
    ]
    return any(el in name.lower() for el in good) and not any(
        el in name.lower() for el in bad
    )
