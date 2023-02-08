# class Auth:
#     def __init__(self):
#         from pathlib import Path
#         import sqlite3 as sqlite
#
#         self.my_db = sqlite.connect('mybase.db')
#         self.cursor = self.my_db.cursor()
#
#     def check_in_db(self):
#
#
#     def db_insert(self):
#         new_data = f"""
#         INSERT VALUES users (name, phone, email)
#         VALUES ('{self.name}' '{self.phone}' '{self.email}')
# """
#         self.cursor.execute(new_data)

from pathlib import Path
import sqlite3 as sql

con = sql.connect('mybase.db')
cur = con.cursor()

# meu_comando = f"""
#     CREATE TABLE users (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         phone TEXT NOT NULL,
#         email TEXT UNIQUE NOT NULL
#     )
# """

# meu_comando = """
#     INSERT INTO users (name, phone, email)
#     VALUES ('Lucas', '923972323', 'mottinha4321@gmail.com')
# """

#
# cur.execute(meu_comando)
# con.commit()
# cur.close()

meu_comando = """
    SELECT email FROM users
    WHERE email = 'luccasdev'
"""

cur.execute(meu_comando)

for i in cur.fetchall():
    print(i)
