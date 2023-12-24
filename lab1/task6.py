# http://www.boredapi.com/api/activity/

import requests

url = 'http://www.boredapi.com/api/activity/'

if __name__ == '__main__':
    data = requests.get(url).json()
    html = f'''<h1>Активность: {data["activity"]}</h1> \n\
    <p>Тип: {data["type"]} К</p>\n\
    <p>Кол-во участников: {data["participants"]}</p>\n\
    <p>Цена: {data["price"]}</p>'''

    with open('lab1/result/task6/result.html', 'w', encoding='utf-8') as output:
        output.write(html)