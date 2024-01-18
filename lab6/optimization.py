from bson.json_util import dumps, loads
import pandas as pd
import json

def get_stat(dataset, filename):
    memory_stat = dataset.memory_usage(deep=True)
    total_memory = memory_stat.sum()
    column_stat = []
    for key in dataset.dtypes.keys():
        column_stat.append({
            'column': key,
            'size': int(memory_stat[key] // 1024),
            'percent_size': memory_stat[key] / total_memory * 100,
            'type': dataset.dtypes[key]
        })
    column_stat.sort(key=lambda x: x['size'], reverse = True)
    column_stat.append({'total_memory': total_memory // 1024})
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(column_stat,  default=str))

def convert_to_categorial(dataframe):
    result = pd.DataFrame()
    dataset_obj = dataframe.select_dtypes(include=['object']).copy()
    for column in dataset_obj.columns:
        if len(dataset_obj[column].unique()) / len(dataset_obj[column]) < 0.5:
            result.loc[:, column] = dataset_obj[column].astype('category')
        else:
            result.loc[:, column] = dataset_obj[column]
    return result

def cast_type(dataframe, from_type,to_type):
    dataset = dataframe.select_dtypes(include=[from_type]).copy()
    return dataset.apply(pd.to_numeric, downcast = to_type)

def optimize_dataset(dataset):
    converted_obj = convert_to_categorial(dataset)
    opt_int = cast_type(dataset,'int','unsigned')
    opt_float = cast_type(dataset,'float','float')
    result = dataset.copy()
    result[converted_obj.columns] = converted_obj
    result[opt_int.columns] = opt_int
    result[opt_float.columns] = opt_float
    return result