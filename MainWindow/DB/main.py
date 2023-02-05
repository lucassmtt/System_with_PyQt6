#DDL -> METADADOS
import sqlite3 as lite

db = lite.connect('mybase.db')
cursor = db.cursor()

comando = """
CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""

cursor.execute(comando)
db.commit()
db.close()