import re
import json
from bs4 import BeautifulSoup

def read_data(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    soup = BeautifulSoup(text, 'html.parser')
    products = soup.find_all('div', attrs={'class': 'product-item'})
    result = list()
    for product in products:
        item = {
            'id': int(product.find_all('a')[0]['data-id']),
            'link': product.find_all('a')[1]['href'],
            'image': product.img['src'],
            'name': product.find('span').get_text().strip(),
            'price': int(product.find('price').get_text().replace('₽', '').replace(' ', '')),
            'bonus': int(product.find('strong').get_text().replace('+ начислим', '').replace('бонусов', ''))
        }
        info = product.ul.find_all('li')
        for param in info:
            item[param['type']] = param.get_text().strip()
        result.append(item)
    return result

if __name__ == '__main__':
    data = list()
    for i in range(1,59):
        filename = f"lab3/data/2/var_75/{i}.html"
        data += read_data(filename)

    data = sorted(data, key=lambda x: x['price'])
    with open('lab3/result/task2/products.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

    filtered_data = list(filter(lambda x: x['bonus'] > 3000, data))         
    with open('lab3/result/task2/products_filtered.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(filtered_data, ensure_ascii=False))

    prices = list(map(lambda x: x['price'], data))         
    prices_stat = {
        'sum': sum(prices),
        'max': max(prices),
        'min': min(prices),
        'avg': sum(prices)/len(prices)
    }
    with open('lab3/result/task2/price_stat.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(prices_stat))

    processors = list()
    for item in data:
        if 'processor' in item.keys():
            processors.append(item['processor'])

    freq = {}
    for item in processors:
        freq[item] = freq.get(item, 0) + 1

    with open('lab3/result/task2/processors_frequency.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(freq, ensure_ascii=False))