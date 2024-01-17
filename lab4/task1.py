import sqlite3
import json

def create_table():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("""
			CREATE TABLE IF NOT EXISTS Game (
			id INTEGER PRIMARY KEY,
			name TEXT NOT NULL,
			city TEXT NOT NULL,
			begin TEXT NOT NULL,
			system TEXT NOT NULL,
			tours_count INTEGER NOT NULL,
			min_rating INTEGER NOT NULL,
			time_on_game INTEGER NOT NULL
			)
			""")

def insert_data():
    with open('lab4/data/task_1_var_75_item.text', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            for item in [[lines[i*9+j].strip().split('::')[-1] for j in range(8)] for i in range(len(lines)//9)]:
                cursor.execute("""
                INSERT INTO Game VALUES (
                :id,
                :name,
                :city,
                :begin, 
                :system,
                :tours_count,
                :min_rating,
                :time_on_game)
                """, item)
        db.commit()
                
def stored_data():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("SELECT * FROM Game ORDER BY tours_count LIMIT 75+10")
            result = [dict(row) for row in cursor.fetchall()]
        with open("lab4/result/task1/sorted.json", "w", encoding="utf-8") as outfile: 
            outfile.write(json.dumps(result, ensure_ascii=False))

def column_stat():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            result = cursor.execute(
				    '''
				    SELECT
				    SUM(min_rating) as sum,
				    MIN(min_rating) as min,
				    MAX(min_rating) as max,
				    AVG(min_rating) as avg
				    FROM Game
				    ''')
        result = [dict(row) for row in cursor.fetchall()]
        with open('lab4/result/task1/stat.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(result, ensure_ascii=False))

def frequency_stat():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("""
            SELECT
            city, COUNT(*) as frequency
            FROM Game
            GROUP BY city
            """)
            result = [dict(row) for row in cursor.fetchall()]
        with open('lab4/result/task1/frequency.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(result, ensure_ascii=False))

def sorted_predicate():
    with sqlite3.connect('lab4/data/base.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("SELECT * FROM Game WHERE tours_count > 10 ORDER BY min_rating LIMIT 75+10")
            result = [dict(row) for row in cursor.fetchall()]
        with open('lab4/result/task1/predicate.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(result, ensure_ascii=False))
if __name__ == "__main__":
    create_table()
    insert_data()
    stored_data()
    column_stat()
    frequency_stat()
    sorted_predicate()