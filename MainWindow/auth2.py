class Auth:
    def __init__(self, Nome, Postname, Email, Phone):
        from pathlib import Path
        import sqlite3 as sql

        self.sql = sql
        self.nome_completo = Nome + Postname
        self.email = Email
        self.phone = Phone
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
                email TEXT UNIQUE NOT NULL
            )
    """
            self.cursor.execute(comando)
            self.connect.commit()
            self.connect.close()

        except Exception as e:
            print(f'ERROR: {e}')


    def db_check(self):
        self.flag = False
        comando = f"""
        SELECT email FROM users
"""
        self.cursor.execute(comando)
        for i in self.cursor.fetchall():
            print(i)
            if i[0] == f'{self.email}':
                print('ok')
                self.flag = True
        self.connect.commit()

        print(self.flag)


    def db_insert(self):

        comando = f"""
        INSERT INTO users (name, phone, email)
        VALUES ('{self.nome_completo}', '{self.phone}', '{self.email}')
        """
        self.cursor.execute(comando)
        self.connect.commit()
        self.connect.close()



a1 = Auth('Joel', 'Mendonça', 'mottinha4321@gmail.com', '3333-2922')
a1.db_check()
