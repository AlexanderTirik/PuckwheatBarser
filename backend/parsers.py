from backend.services import (
    clean_weight, parse_weight, get_soup,
    parse_source_from_name, clean_name,
    fixed_price_format, is_buckwheat
)
from backend.urls import (
    EPICENTRK_HOST, AUCHAN_HOST
)
from backend.shop_names import (
    FOZZY, EPICENTRK, AUCHAN
)


def parse_fozzy(response):
    """
    Parse buckwheat from fozzy
    """
    soup = get_soup(response)
    products = soup.find_all('div', class_='js-product-miniature-wrapper')

    data = []
    for product in products:
        try:
            description = product.find('div', class_='product-description')

            price = description.find('span', class_='product-price').get('content')
            price = fixed_price_format(price)
            name = description.find('div', class_='h3 product-title').a.get_text()
            name = clean_name(name)
            if not is_buckwheat(name):
                continue
            source = description.find('div', class_='product-brand').a.get_text()
            product_url = description.find('div', class_='h3 product-title').a.get('href')
            img_url = product.find('div', class_='thumbnail-container').a.img.get('src')
            weight = product.find('div', class_='product-reference text-muted').a.get_text().replace('Фасовка: ',
                                                                                                     '').strip()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)
            
            data.append({
                'price': price,
                'name': name,
                'source': source,
                'productUrl': product_url,
                'imgUrl': img_url,
                'shop': FOZZY,
                'weight': weight
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data


def parse_epicentrk(response):
    """
    Parse buckwheat from epicentrk
    """
    soup = get_soup(response)
    products = soup.find_all('div', class_='card-wrapper')

    data = []
    for product in products:
        try:
            name = product.find('div', class_='card__name').a.b.get_text().strip()
            name = clean_name(name)
            if not is_buckwheat(name):
                continue
            price = product.find('span', class_='card__price-sum').contents[0].strip()
            price = fixed_price_format(price)
            source = product.find('ul', class_='card__characteristics').find_all('li')[1].get_text().replace('Бренд:',
                                                                                                             '').strip()
            product_url = EPICENTRK_HOST + product.find('a', class_='card__photo').get('href')
            img_url = product.find('a', class_='card__photo').img.get('src')
            weight = product.find('ul', class_='card__characteristics').find_all('li')[2].get_text().replace('Вага:',
                                                                                                             '').strip()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)
            
            data.append({
                'price': price,
                'name': name,
                'source': source,
                'productUrl': product_url,
                'imgUrl': img_url,
                'shop': EPICENTRK,
                'weight': weight
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data


def parse_auchan(response):
    """
    Parse buckwheat from auchan
    """
    soup = get_soup(response)
    products = soup.find_all('div', class_='products-box__list-item')
    
    data = []
    for product in products:
        try:
            price = product.find('span', class_='Price__value_caption').get_text()
            price = fixed_price_format(price)
            name = product.a.get('title')
            name = clean_name(name)
            if not is_buckwheat(name):
                continue
            source = parse_source_from_name(name, default_name=AUCHAN)
            product_url = AUCHAN_HOST + product.find('a', class_='product-tile').get('href')
            img_url = product.find('img', class_='product-tile__image-i').get('src')
            weight = product.find('div', class_='product-tile__title-wrapper').find('div').get_text()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)
            
            data.append({
                'price': price,
                'name': name,
                'source': source,
                'productUrl': product_url,
                'imgUrl': img_url,
                'shop': AUCHAN,
                'weight': weight
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data
