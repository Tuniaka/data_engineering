# для корректной работы необходимо распаковать архивы
import re
import json
from bs4 import BeautifulSoup

def read_data(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    soup = BeautifulSoup(text, 'html.parser')
    body = soup.find('body')
    competition = dict()
    competition['type'] = body.find('span', string=re.compile('Тип:')).get_text().replace('Тип:', '').strip()
    competition['title'] = body.find("h1", attrs={"class": "title"}).get_text().replace('Турнир:', '').strip()
    competition['year'] = int(competition['title'].split(' ')[-1])
    address = body.find('p', attrs={'class': 'address-p'}).get_text().replace('Город:', '').split('Начало:')
    competition['city'] = address[0].strip()
    competition['date'] = address[1].strip()
    competition['count'] = int(body.find("span", attrs={"class": "count"}).get_text().replace('Количество туров:', ''))
    competition['time_limit'] = int(body.find("span", attrs={"class": "year"}).get_text().replace('Контроль времени:', '').replace('мин', ''))
    competition['min_rating'] = int(body.find('span', string=re.compile('Минимальный рейтинг для участия:')).get_text().replace('Минимальный рейтинг для участия:', '').strip())
    competition['image'] = body.find("img")['src']
    competition['rating'] = float(body.find("span", string=re.compile('Рейтинг:')).get_text().replace('Рейтинг:', ''))
    competition['views'] = int(body.find("span", string=re.compile('Просмотры:')).get_text().replace('Просмотры:', ''))
    return competition

if __name__ == '__main__':
    competition_info = list()
    for i in range(1, 1000):
        filename = f"lab3/data/1/var_75/{i}.html"
        competition_info.append(read_data(filename))

    competition_info = sorted(competition_info, key=lambda x: x['year'], reverse=True)
    with open('lab3/result/task1/sorted_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(competition_info, ensure_ascii=False))

    filtered_data = list(filter(lambda x: x['min_rating'] < 2500, competition_info))         
    with open('lab3/result/task1/filtered_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(filtered_data, ensure_ascii=False))

    rate = list(map(lambda x: x['rating'], competition_info))         
    rating_stat = {
        'sum': round(sum(rate), 2),
        'max': round(max(rate), 2),
        'min': round(min(rate), 2),
        'average': round(sum(rate)/len(rate), 4)
    }
    with open('lab3/result/task1/rating_stat.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(rating_stat, ensure_ascii=False))

    freq = {}
    for type in list(map(lambda x: x['type'], competition_info)):
        freq[type] = freq.get(type, 0) + 1

    with open('lab3/result/task1/freq_of_types.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(freq, ensure_ascii=False))