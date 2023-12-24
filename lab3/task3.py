from bs4 import BeautifulSoup
import re
import json

def read_data(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    soup = BeautifulSoup(text, 'xml')
    star = soup.find('star')
    result = dict()
    for tag in ['name', 'constellation', 'spectral-class']:
        result[tag] = star.find(tag).get_text().strip()
    for tag in ['rotation', 'age', 'distance', 'absolute-magnitude']:
        result[tag] = float(star.find(tag).get_text().split()[0].strip())
    result['radius'] = int(star.find('radius').get_text())
    return result

if __name__ == '__main__':
    data = list()
    for i in range(1, 501):
        filename = f"lab3/data/3/var_75/{i}.xml"
        data.append(read_data(filename))

    data = sorted(data, key=lambda x: x['distance'])
    with open('lab3/result/task3/stars_info.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

    filtered_data = list(filter(lambda x: x['age'] < 3, data))         
    with open('lab3/result/task3/filtered_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(filtered_data, ensure_ascii=False))
        
    stars_radius = list(map(lambda x: x['radius'], data))         
    radius_stat = {
        'sum': sum(stars_radius),
        'max': max(stars_radius),
        'min': min(stars_radius),
        'avg': round(sum(stars_radius)/len(stars_radius), 3)
    }
    with open('lab3/result/task3/radius_stat.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(radius_stat, ensure_ascii=False))

    freq = {}
    for item in list(map(lambda x: x['constellation'], data)):
        freq[item] = freq.get(item, 0) + 1

    with open('lab3/result/task3/freq_constellations.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(freq, ensure_ascii=False))