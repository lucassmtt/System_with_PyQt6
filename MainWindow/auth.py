class Auth:
    def __init__(self,Nome, Postname, Email, Phone):
        from pathlib import Path
        import sqlite3 as sql

        self.sql = sql
        self.nome_completo = Nome + Postname
        self.email = Email
        self.phone = Phone
        self.PATH_DB = Path().absolute() / 'DB' / 'mybase.db'
        self.connect = self.sql.connect(self.PATH_DB)
        self.cursor = self.connect.cursor()


        print(self.PATH_DB)

        try:
            from pathlib import Path
            self.PATH_DB = PATH_DB = Path().absolute() / 'DB' / 'mybase.db'

            comando = """
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
            print('Tabela já criada')


    def connect_execute_commit_close(self, func):
        def decorador(self, *args):
            sql = func(*args)
            self.cursor.execute(sql)
            self.connect.commit()
            self.connect.close()

        return decorador


    # @connect_execute_commit_closesssss
    def db_insert(self):
        # try:
        new_data = f"""
        INSERT INTO users (name, phone, email)
        VALUES('{self.nome_completo}''{self.phone}''{self.email}')"""

        # except Exception as e:
        print(f'Dados inseridos ')


    # @connect_execute_commit_close
    def db_update(self, dado_a_ser_mudado, novo_dado, id, key):
        try:
            new_data = f"""
            UPDATE users SET({dado_a_ser_mudado} = '{novo_dado}' WHERE {id} = '{key}')"""

        except Exception as e:
            print(f'Impossível atualizar dados: ')


    # @connect_execute_commit_close
    def db_delete(self, id, key_del):
        try:
            data_delete = f"""
            DELETE FROM users WHERE '{id}'={key_del}"""
            print('Dados deletados')

        except Exception as e:
            print(f'Impossível deletar dados: ')

    def db_select(self, data, field):
        connect = self.sql.connect(self.PATH_DB)
        cursor = connect.cursor()
        search = f"""
        SELECT id, name, phone, email
        FROM users {field} = {data}
"""



A1 = Auth('Lucas', 'Motta', 'mottinha', '4798828222')
A1.db_insert()

