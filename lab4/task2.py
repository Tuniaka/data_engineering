import sqlite3
import json
import msgpack

def create_table():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("""
			CREATE TABLE IF NOT EXISTS Awards (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			place INTEGER NOT NULL,
			prise INTEGER NOT NULL
			)
			""")

def insert_data():
    with sqlite3.connect('lab4/data/base.db') as db:
        with open("lab4/data/task_2_var_75_subitem.json", encoding='utf-8') as file:
            data = json.load(file)
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.executemany(
                """
				INSERT INTO Awards (name, place, prise)
				VALUES(:name, :place, :prise)
				""", data)
        db.commit()

def query_for_tables():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            insert_query = ("""
                            SELECT MAX(prise) FROM Game JOIN Awards
							ON Game.name = Awards.name WHERE min_rating > 2200
                            """)
            cursor.execute(insert_query)
            result1 = [dict(row) for row in cursor.fetchall()]

            insert_query = ("""
                            SELECT AVG(tours_count) FROM Game JOIN Awards
							ON Game.name = Awards.name WHERE prise > 500000
                            """)
            cursor.execute(insert_query)
            result2 = [dict(row) for row in cursor.fetchall()]

            insert_query = ("""
                            SELECT * FROM Game JOIN Awards
							ON Game.name = Awards.name WHERE place < 2
                            """)
            cursor.execute(insert_query)
            result3 = [dict(row) for row in cursor.fetchall()]

        with open("lab4/result/task2/query1.json", "w", encoding="utf-8") as outfile: 
            outfile.write(json.dumps(result1, ensure_ascii=False)[1:-1])
        with open("lab4/result/task2/query2.json", "w", encoding="utf-8") as outfile: 
            outfile.write(json.dumps(result2, ensure_ascii=False)[1:-1])
        with open("lab4/result/task2/query3.json", "w", encoding="utf-8") as outfile: 
            outfile.write(json.dumps(result3, ensure_ascii=False)[1:-1])

if __name__=="__main__":
    create_table()
    insert_data()
    query_for_tables()