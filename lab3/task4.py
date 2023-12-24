import json
from bs4 import BeautifulSoup

def read_data(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    soup = BeautifulSoup(text, 'xml')
    info = list()
    products = soup.find_all('clothing')
    for product in products:
        item = {
            'id': int(product.find('id').get_text()),
            'name': product.find('name').get_text().strip(),
            'category': product.find('category').get_text().strip(),
            'size': product.find('size').get_text().strip(),
            'color': product.find('color').get_text().strip(),
            'material': product.find('material').get_text().strip(),
            'price': int(product.find('price').get_text().strip()),
            'rating': float(product.find('rating').get_text().strip()),
            'reviews': int(product.find('reviews').get_text().strip()),
        }
        for param in ['new', 'exclusive', 'sporty']:
            if product.find(param):
                item[param] = product.find(param).get_text().strip() in ['+', 'yes']    
        info.append(item)
    return info

data = list()
for i in range(1,101):
    filename = f"lab3/data/4/var_75/{i}.xml"
    data += read_data(filename)

product_data = sorted(data, key=lambda x: x['rating'], reverse=True)
with open('lab3/result/task4/products_data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, ensure_ascii=False))

filtered_data = list(filter(lambda x: 'new' in x.keys() and x['new'], product_data))         
with open('lab3/result/task4/result_filtered.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(filtered_data, ensure_ascii=False))

prices = list(map(lambda x: x['price'], product_data))         
prices_stat = {
    'sum': sum(prices),
    'max': max(prices),
    'min': min(prices),
    'avg': round(sum(prices)/len(prices), 3)
}
with open('lab3/result/task4/price_stat.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(prices_stat))

freq = {}
for item in list(map(lambda x: x['material'], product_data)):
    freq[item] = freq.get(item, 0) + 1

with open('lab3/result/task4/material_freq.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(freq, ensure_ascii=False))
