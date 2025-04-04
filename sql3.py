import sqlite3

conexao = sqlite3.connect(database = 'base.db',
                          timeout = 5,
                          detect_types = sqlite3.PARSE_COLNAMES,
                          isolation_level= 'DEFERRED')

cursor = conexao.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT
               'Num Telefone' TEXT
               Prosissão TEXT
               )
               ''')

conexao.commit()