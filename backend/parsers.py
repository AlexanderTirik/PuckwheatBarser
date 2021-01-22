from backend.services import (
    clean_weight, parse_weight, get_soup
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
            name = description.find('div', class_='h3 product-title').a.get_text()
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
            source = product.find('ul', class_='card__characteristics').find_all('li')[1].get_text().replace('Бренд:',
                                                                                                             '').strip()
            product_url = host + product.find('a', class_='card__photo').get('href')
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
                'shop': shop,
                'weight': weight,
                'weightValue': weight_value
            })
        except Exception as e:
            print(f'Something was wrong: {e}')

    return data
