import pymongo
import msgpack

if __name__ == "__main__":
	client = pymongo.MongoClient()
	db = client['task_db']
	collection = db['db']
	with open('lab5/data/task_3_item.msgpack', "rb") as file:
		data = msgpack.unpack(file)
		for row in data:
			collection.insert_one(row)

	collection.delete_many({'$or': [{'salary': {'$lt': 25000}}, {'salary': {'$gt': 175000}}]})
	collection.update_many({}, {'$inc': {'age': 1}})
	collection.update_many({'profession': {'$in': ['Учитель', 'Строитель']}}, {'$mul': {'salary': 1.05}})
	collection.update_many({'city': {'$in': ['Сьюдад-Реаль', 'Любляна']}}, {'$mul': {'salary': 1.07}})
	collection.update_many({'$and': [{'city': 'Гранада'}, {'profession': {'$in': ['Учитель','Строитель']}},
									 {'age': {'$gt': 30, '$lt': 50}}]}, {'$mul': {'salary': 1.1}})
	collection.delete_many({'salary': {'$gt': 90000}})

