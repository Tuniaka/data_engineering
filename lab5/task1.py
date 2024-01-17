import pymongo
import pickle
from pprint import pprint

if __name__ == "__main__":
	objects = []
	with open('lab5/data/task_1_item.pkl', 'rb') as f:
		data = pickle.load(f)

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
	db.drop_collection('db')
	collection = db['db']
	for record in objects:
		collection.insert_one(record)

	result = collection.find().sort('salary', pymongo.DESCENDING).limit(10)
	pprint(list(result))

	result = collection.find({'age': {'$lt': 30}}).sort('salary', pymongo.DESCENDING).limit(15)
	pprint(list(result))

	result = (
		collection.find(
			{'$and': [{'city': 'Аликанте'}, {'job': {'$in': ['Продавец', 'Бухгалтер', 'Повар']}}]}).sort(
			'age', pymongo.ASCENDING).limit(10))
	pprint(list(result))

	result = collection.count_documents({'$and': [{'age': {'$gte': 30, '$lte': 50}},
												{'year': {'$in': [2019, 2020, 2021, 2022]}}, {
												'$or': [{'salary': {'$gt': 50000, '$lte': 75000}},
												{'salary': {'$gt': 125000, '$lt': 150000}}]}]})
	pprint(result)