class login_db:
    def __init__(self):
        import sqlite3 as sql

        PATH_DB = 'primeiro_banco.db'
        db = sql.connect(PATH_DB)
