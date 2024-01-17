import pymongo
import json
from bson.json_util import dumps, loads

if __name__ == "__main__":
	objects = []
	with open('lab5/data/task_2_item.json', encoding='utf-8') as f:
		data = json.load(f)
	for item in data:
		record = {}
		record['id'] = item['id']
		record['age'] = int(item['age'])
		record['city'] = item['city']
		record['job'] = item['job']
		record['salary'] = int(item['salary'])
		record['year'] = int(item['year'])
		objects.append(record)

	client = pymongo.MongoClient()
	db = client['task_db']
	collection = db['db']
	collection.insert_many(objects)

	query = collection.aggregate(
		[{'$group':{'_id': None,
			        'min': {'$min': '$salary'},
					'avg': {'$avg': '$salary'},
					'max': {'$max': '$salary'}}}])
	result = list(query)
	with open('lab5/result/task2/res1.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$group':{'_id': '$profession',
			        'count': {'$sum': 1}}}])
	result = list(query)
	with open('lab5/result/task2/res2.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))
		
	query = collection.aggregate(
		[{'$group':{'_id': '$city',
					'min_salary': {'$min': '$salary'},
					'avg': {'$avg': '$salary'},
					'min': {'$max': '$salary'}}}])
	result = list(query)
	with open('lab5/result/task2/res2.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$group':{'_id': '$job',
					'min': {'$min': '$salary'},
					'avg': {'$avg': '$salary'},
					'max': {'$max': '$salary'}}}])
	result = list(query)
	with open('lab5/result/task2/res3.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$group':{'_id': '$city',
					'min': {'$min': '$age'},
					'avg': {'$avg': '$age'},
					'max': {'$max': '$age'}}}])
	result = list(query)
	with open('lab5/result/task2/res4.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$group':{'_id': '$job',
					'min': {'$min': '$age'},
					'avg': {'$avg': '$age'},
					'max_age': {'$max': '$age'}}}])
	result = list(query)
	with open('lab5/result/task2/res5.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate([{'$sort': {'age': 1,
                                            'salary': -1
                                            }},{'$limit': 1}])
	result = list(query)
	with open('lab5/result/task2/res6.json', 'w', encoding='utf-8') as outfile:
		outfile.write(dumps(result, ensure_ascii=False))

	query = collection.aggregate([{'$sort': {'age': -1,
                                            'salary': 1
                                            }},{'$limit': 1}])
	result = list(query)
	with open('lab5/result/task2/res7.json', 'w', encoding='utf-8') as outfile:
		outfile.write(dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$match':{'salary': {'$gt': 50000}}},
			       {'$group': {'_id': '$city',
					           'min': {'$min': '$age'},
					           'avg': {'$avg': '$age'},
					           'max': {'$max': '$age'}}},
			       {'$sort': {'name': pymongo.ASCENDING}}])
	result = list(query)
	with open('lab5/result/task2/res8.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$match':{'$or':[{'age':{'$gt': 18, '$lt': 25}},
							{'age':{'$gt': 50, '$lt': 65}}]}},
         {'$group':{'_id': {'city': '$city', 'job': '$job'},
					'min': {'$min': '$salary'},
					'avg': {'$avg': '$salary'},
					'max': {'$max': '$salary'}}}])
	result = list(query)
	with open('lab5/result/task2/res9.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))

	query = collection.aggregate(
		[{'$match': {'year': {'$lt': 2015}}},
        {'$group': {
                '_id': '$job',
                'max_salary': {'$max': '$salary'},
            }},
        {'$sort': {'max_salary': -1}}
    ])
	result = list(query)
	with open('lab5/result/task2/res10.json', 'w', encoding='utf-8') as outfile:
		outfile.write(json.dumps(result, ensure_ascii=False))