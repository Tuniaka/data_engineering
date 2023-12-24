import csv

data = []
sum = 0
const = 25 + 75 % 10

if __name__ == '__main__':
    with open('lab1/data/text_4_var_75', newline='\n', encoding='utf-8') as file:
        for row in csv.reader(file, delimiter=','):
            item = {
                'id': int(row[0]),
                'name': f"{row[1]} {row[2]}",
                'age': int(row[3]),
                'salary': int(row[4].replace('₽', ''))
            }
            data.append(item)
            sum += item['salary']
        
    ave = sum / len(data)    
    res = filter(lambda item: item['age'] > const and item['salary'] > ave, data)
    res = sorted(res, key = lambda item: item['id'])

    with open('lab1/result/task4/result', 'w', encoding='utf-8', newline='') as output:
        writer = csv.writer(output,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in res:
            writer.writerow(item.values())