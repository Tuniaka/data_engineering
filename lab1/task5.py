import csv
from bs4 import BeautifulSoup

rows = []
top = []

if __name__ == '__main__':
    with open('lab1/data/text_5_var_75', 'r') as file:
        html = file.read()

    data = BeautifulSoup(html, 'html.parser').find('table')

    for header in data.find_all('th'):
        top.append(header.text)

    for row in data.find_all('tr'):
        rows.append([data.text for data in row.find_all('td')])

    with open('lab1/result/task5/result.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(top)
        writer.writerows(rows)