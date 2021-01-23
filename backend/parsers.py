from backend.services import (
    clean_weight, parse_weight, get_soup, parse_source_from_name, clean_name, fixed_price_format, check_is_packed
)


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
            price = fixed_price_format(price)
            name = description.find('div', class_='h3 product-title').a.get_text()
            name = clean_name(name)
            source = description.find('div', class_='product-brand').a.get_text()
            product_url = description.find('div', class_='h3 product-title').a.get('href')
            img_url = product.find('div', class_='thumbnail-container').a.img.get('src')
            weight = product.find('div', class_='product-reference text-muted').a.get_text().replace('Фасовка: ',
                                                                                                     '').strip()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)
            is_packed, source = check_is_packed(source, default_source=shop)
            
            data.append({
                'price': price,
                'name': name,
                'source': source,
                'productUrl': product_url,
                'imgUrl': img_url,
                'shop': shop,
                'weight': weight,
                'weightValue': weight_value,
                'is_packed': is_packed,
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
            name = clean_name(name)
            price = product.find('span', class_='card__price-sum').contents[0].strip()
            price = fixed_price_format(price)
            source = product.find('ul', class_='card__characteristics').find_all('li')[1].get_text().replace('Бренд:',
                                                                                                             '').strip()
            product_url = host + product.find('a', class_='card__photo').get('href')
            img_url = product.find('a', class_='card__photo').img.get('src')
            weight = product.find('ul', class_='card__characteristics').find_all('li')[2].get_text().replace('Вага:',
                                                                                                             '').strip()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)
            is_packed, source = check_is_packed(source, default_source=shop)
            
            data.append({
                'price': price,
                'name': name,
                'source': source,
                'productUrl': product_url,
                'imgUrl': img_url,
                'shop': shop,
                'weight': weight,
                'weightValue': weight_value,
                'is_packed': is_packed,
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data


async def parse_auchan():
    """
    Parse buckwheat from auchan
    """
    url = 'https://auchan.zakaz.ua/uk/categories/buckwheat-auchan/'
    host = 'https://auchan.zakaz.ua'
    shop = 'Ашан'

    soup = await get_soup(url)
    products = soup.find_all('div', class_='products-box__list-item')
    
    data = []
    for product in products:
        try:
            price = product.find('span', class_='Price__value_caption').get_text()
            price = fixed_price_format(price)
            name = product.a.get('title')
            name = clean_name(name)
            source = parse_source_from_name(name)
            product_url = host + product.find('a', class_='product-tile').get('href')
            img_url = product.find('img', class_='product-tile__image-i').get('src')
            weight = product.find('div', class_='product-tile__title-wrapper').find('div').get_text()
            weight = clean_weight(weight)
            weight_value = parse_weight(weight)
            is_packed, source = check_is_packed(source, default_source=shop)
            
            data.append({
                'price': price,
                'name': name,
                'source': source,
                'productUrl': product_url,
                'imgUrl': img_url,
                'shop': shop,
                'weight': weight,
                'weightValue': weight_value,
                'is_packed': is_packed,
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data
