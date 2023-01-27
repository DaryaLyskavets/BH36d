import sqlite3
from csv import reader, DictReader

conn = sqlite3.connect('students.sqlite3')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (24) NOT NULL,
    surname VARCHAR (24) NOT NULL 
    );
''')
conn.commit()

with open(r'C:\Users\Admin\Desktop\students.csv', mode='r', encoding='utf-8') as file:
    r = DictReader(file, delimiter=';')
    to_db = [(i['name'], i['surname']) for i in r]

cur.executemany('''
    INSERT INTO students (name, surname)
    VALUES(?, ?);
''', to_db)
conn.commit()