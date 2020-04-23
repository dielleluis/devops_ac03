import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()
c.execute('''CREATE TABLE info
            (id integer, nome text not null, email text, primary key(id))''')

c.execute('''INSERT INTO info VALUES
            (1902448, 'LUIS DIELLE', 'luis.dielle@hasl.com')''')

'''c.execute("PRAGMA table_info('info')")'''

'''c.execute("PRAGMA table_info('info')").fetchall()'''

for row in c.execute("PRAGMA table_info('info')").fetchall():
    print('Nome dos Campos:', row[1])
    print('PK:', row[0])
    print('Not Null:', row[3])


