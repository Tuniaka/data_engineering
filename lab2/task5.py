# ссылка на open_data.csv https://disk.yandex.ru/d/zt_teap33StlMg
import csv, msgpack, os, pickle, json
import pandas as pd

def read_all_data(path):
    data = pd.read_csv(path, low_memory=False)
    data = data[['ID ведомства из ФРГУ', 'Название ведомства', 'ID услуги из ФРГУ', 'Название услуги',
                  'Значение показателя','Наименование оцениваемого критерия (показателя)', 'Единицы измерения оценки (показателя)']]
    data = data.rename(columns = {'ID ведомства из ФРГУ': 'department_id', 'Название ведомства': 'department_name', 'ID услуги из ФРГУ': 'service_id',
                                  'Название услуги': 'service_name', 'Значение показателя': 'index_value', 'Наименование оцениваемого критерия (показателя)':'criterion',
                                  'Единицы измерения оценки (показателя)':'units'})
    calculation_data(data)

def calculation_data(data):
    res = {}
    
    for column in data.columns:
        if column != 'index_value':
            clmn = dict(data[column].value_counts())
            for key, value in clmn.items():
                clmn[key] = int(value)
            res[column] = clmn

    res['inx_value_max'] = (int(data['index_value'].max()))
    res['inx_value_min'] = (int(data['index_value'].min()))
    res['inx_ave'] = round(data['index_value'].mean(), 2)
    res['inx_sum'] = round(data['index_value'].sum())
    res['inx_std'] = round(data['index_value'].std(), 2)

    save_data(res)

def save_data(res):
    with open("lab2/result/task5/result.json", "w") as f:
        f.write(json.dumps(res))

    with open("lab2/result/task5/result.msgpack", "wb") as f:
        f.write(msgpack.dumps(res))

    with open("lab2/result/task5/result.pkl", "wb") as f:
        f.write(pickle.dumps(res))

    with open('lab2/result/task5/result.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(res.keys())
        writer.writerow(res.values())
        
    print(f"size of msgpack file: {round(os.path.getsize('lab2/result/task5/result.msgpack') / 1024, 2)} KB")
    print(f"size of csv file:     {round(os.path.getsize('lab2/result/task5/result.csv') / 1024, 2)} KB")
    print(f"size of pkl file:     {round(os.path.getsize('lab2/result/task5/result.pkl') / 1024, 2)} KB")
    print(f"size of json file:    {round(os.path.getsize('lab2/result/task5/result.json') / 1024, 2)} KB")


if __name__ == '__main__':
    read_all_data('lab2/data/open_data.csv')