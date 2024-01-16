import msgpack
import pandas as pd
import sqlite3
import json

def read_csv():
    data = pd.read_csv('lab4/data/task_3_var_75_part_1.csv', delimiter=';')
    data = data.to_dict("records")
    for row in data:
        row.pop('energy')
        row.pop('key')
        row.pop('loudness')
    return data

def read_msgpack():
    with open("lab4/data/task_3_var_75_part_2.msgpack", "rb") as file:
        data = msgpack.unpack(file)
    for row in data:
        row.pop('mode')
        row.pop('speechiness')
        row.pop('acousticness')
        row.pop('instrumentalness')

    return data

def create_base():
    with sqlite3.connect('lab4/data/task3.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS MusicData (
                id          INTEGER     PRIMARY KEY AUTOINCREMENT,
                artist      TEXT,
                song        TEXT,
                duration_ms INTEGER,
                year        INTEGER,
                tempo       REAL,
                genre       TEXT
                )
                """)

def insert_data(data):
    with sqlite3.connect('lab4/data/task3.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
    cursor.executemany("""
                       INSERT INTO MusicData (
                       artist, song, duration_ms, 
                       year, tempo, genre)
                       VALUES (
                       :artist, :song, :duration_ms, 
                       :year, :tempo, :genre
                       )
                       """, 
                       data)
    db.commit()

def sort_tempo():
    with sqlite3.connect('lab4/data/task3.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
           select_query = "SELECT * FROM MusicData ORDER BY tempo LIMIT 85"
           cursor.execute(select_query)
           result = [dict(row) for row in cursor.fetchall()]
    with open('lab4/result/task3/sort_tempo.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(result, ensure_ascii=False)[1:-1])

def get_stat():
    with sqlite3.connect('lab4/data/task3.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute('''
					    SELECT
						SUM(year) as sum,
						MIN(year) as min,
						MAX(year) as max,
						AVG(year) as avg
						FROM MusicData
				        ''')
            result = [dict(row) for row in cursor.fetchall()]
        with open('lab4/result/task3/stat_data.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(result, ensure_ascii=False)[1:-1])

def get_freq():
    with sqlite3.connect('lab4/data/task3.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("""SELECT
                        artist, COUNT(*) as frequency
                        FROM MusicData
                        GROUP BY artist
                        ORDER BY frequency DESC
                           """)
    result = [dict(row) for row in cursor.fetchall()]
    with open('lab4/result/task3/frequency.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(result, ensure_ascii=False)[1:-1])

def get_filter():
    with sqlite3.connect('lab4/data/task3.db') as db:
        cursor = db.cursor()
        cursor.row_factory = sqlite3.Row
        with db:
            cursor.execute("""
                           SELECT * FROM MusicData 
                           WHERE tempo < 90.0 
                           ORDER BY duration_ms LIMIT 90
                           """)
    result = [dict(row) for row in cursor.fetchall()]
    with open('lab4/result/task3/filtered.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(result, ensure_ascii=False)[1:-1])

if __name__=="__main__":
    create_base()
    insert_data(read_csv())
    insert_data(read_msgpack())
    sort_tempo()
    get_stat()
    get_freq()
    get_filter()
