import sqlite3
import json
import msgpack

def create_db():
	with open('lab4/data/task_4_var_75_product_data.json', encoding='utf-8') as f:
		data = json.load(f)

	with sqlite3.connect('lab4/data/task4.db') as db:
		cursor = db.cursor()
		cursor.row_factory = sqlite3.Row
		with db:
				cursor.execute('''
				CREATE TABLE IF NOT EXISTS ComputerData(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT,
				price INTEGER,
				quantity INTEGER,
				fromCity TEXT,
				isAvailable TEXT,
				views INTEGER,
				count INTEGER DEFAULT 0
				)
				''')
				cursor.executemany('''
					    INSERT INTO ComputerData (name, price, quantity, views, fromCity, isAvailable)
					    VALUES(
					    	:name, :price, :quantity, :fromCity, :isAvailable, :views)
					    ''', data)
				
def update_db():
	with open("lab4/data/task_3_var_75_part_2.msgpack", "rb") as f:
		data = msgpack.unpack(f)
	with (sqlite3.connect('lab4/data/task4.db') as db):
		cursor = db.cursor()
		cursor.row_factory = sqlite3.Row
		with db:
			pass
				
if __name__=="__main__":
    # create_db()
	# update_db()
	pass