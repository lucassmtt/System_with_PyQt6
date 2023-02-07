class Auth:
    def __init__(self,Nome, Postname, Email, Phone, PATH_DB):
        from pathlib import Path
        import sqlite3 as sql

        self.sql = sql
        self.nome_completo = Nome + Postname
        self.email = Email
        self.phone = Phone
        self.PATH_DB = Path().absolute() / 'DB' / 'mybase.db'


        print(self.PATH_DB)

        try:
            from pathlib import Path
            self.PATH_DB = PATH_DB = Path().absolute() / 'DB' / 'mybase.db'
            db = self.sql.connect(self.PATH_DB)
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

        except sql.OperationalError:
            print('Tabela já criada')


    def connect_execute_commit_close(self, func):
        def decorador(self, *args):
            connect = self.sql.connect(self.)


    @connect_execute_commit_close
    def db_insert(self):
        # try:
        new_data = f"""
        INSERT INTO users (name, phone, email)
        VALUES('{self.nome_completo}''{self.phone}''{self.email}')"""

        # except Exception as e:
        print(f'Impossível inserir dados: {e}')


    @connect_execute_commit_close
    def db_update(self, dado_a_ser_mudado, novo_dado, id, key):
        try:
            new_data = f"""
            UPDATE users SET({dado_a_ser_mudado} = '{novo_dado}' WHERE {id} = '{key}')"""

        except Exception as e:
            print(f'Impossível atualizar dados: {e}')


    @connect_execute_commit_close
    def db_delete(self, id, key_del):
        try:
            data_delete = f"""
            DELETE FROM users WHERE '{id}'={key_del}"""

        except Exception as e:
            print(f'Impossível deletar dados: {e}')

    def db_select(self, data, field):
        connect = self.sql.connect(self.PATH_DB)
        cursor = connect.cursor()
        search = f"""
        SELECT id, name, phone, email
        FROM users {field} = {data}
"""



# a1 = Auth('Lucas', 'Motta', 'motta@gmail.com', '932929372')






































