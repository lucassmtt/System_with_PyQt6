class Auth:
    def __init__(self):
        from pathlib import Path
        import sqlite3 as sql
        self.sql = sql

        self.name = None
        self.email = None
        self.password = None
        self.phone = None

        self.PATH_DB = Path().absolute() / 'DB' / 'mybase.db'
        self.connect = self.sql.connect(self.PATH_DB)
        self.cursor = self.connect.cursor()
        self.flag = False

        try:
            comando = f"""
            CREATE TABLE users (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL, 
                email TEXT UNIQUE NOT NULL,
                password TEXT UNIQUE NOT NULL
            ) """
            self.cursor.execute(comando)
            self.connect.commit()
            self.connect.close()

        except Exception as e:
            print(f'ERROR: {e}')


    def db_insert(self, name, phone, email, password):
        new_user = f"""
        INSERT INTO users (name, phone, email, password)
        VALUES ('{name}', {phone}, '{email}', '{password}')
    """
        self.cursor.execute(new_user)
        self.connect.commit()
        self.connect.close()



    def db_login(self, email, password):
        flag_email = False
        flag_senha = False

        comando_email = f"""SELECT email, password FROM users"""
        comando_password = f"""SELECT password, password FROM users"""

        self.cursor.execute(comando_email)
        for i in self.cursor.fetchall():
            if i[0] == f'{email}':
                flag_email = True

        self.cursor.execute(comando_password)
        for i in self.cursor.fetchall():
            if i[0] == f'{password}':
                flag_senha = True

        if flag_senha and flag_email == True:
            return 1
        else:
            return 2

