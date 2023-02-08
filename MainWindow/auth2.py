import sqlite3


class Auth:
    def __init__(self, Nome, Postname, Email, Phone):
        from pathlib import Path
        import sqlite3 as sql

        self.sql = sql
        self.nome_completo = Nome + Postname
        self.email = Email
        self.phone = Phone
        self.PATH_DB = Path().absolute() / 'DB' / 'mybase.db'

        self.connect = sql.connect(self.PATH_DB)
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

        except sql.OperationalError:
            print('Falha ou tabela criada')


    def db_check(self):
        comando = f"""
        SELECT email FROM users
        WHERE email = '{self.email}'
"""
        self.cursor.execute(comando)
        self.cursor.fetchone()

        # if i[0] == self.email:
        #     print('Email criado')
        #     self.flag = True
        #     return self.flag
        # else:
        #     return self.flag


    def db_insert(self):
        if self.flag:
            pass
        else:
            comando = f"""
            INSERT INTO users (name, phone, email)
            VALUES ('{self.nome_completo}', '{self.phone}', '{self.email}')
            """
            self.cursor.execute(comando)
            self.connect.commit()
            self.connect.close()



a1 = Auth('Lucas', 'Gabriel', 'lucasmotinha', '2921-2922')
a1.db_check()
