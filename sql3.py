import sqlite3

conexao = sqlite3.connect(database = 'base.db',
                          timeout = 5,
                          detect_types = sqlite3.PARSE_COLNAMES,
                          isolation_level= 'DEFERRED')

cursor = conexao.cursor()

cursor.execute('''
             CREATE TABLE IF NOT EXISTS Usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               email TEXT,
               'num telefone' TEXT,
               profissao TEXT
               )
''')


cursor.execute("INSERT INTO Usuarios (nome, email, profissao)VALUES (?, ?, ?)",
               ('João Pereira Pinto', 'Joao_programmingJava@uol.com', 'Programador Full-Stack'))

conexao.commit()

