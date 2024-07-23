import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'Customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

#registar valores na tabela

cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id,name,weight)'
    'VALUES (NULL, "Maria", 4),(NULL, "Helena",9.9)'
)
connection.commit()


# SQL

cursor.close()
connection.close()



