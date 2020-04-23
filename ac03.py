import sqlite3

conn = sqlite3.connect('info.db')

c = conn.cursor()
c.execute('''CREATE TABLE info
            (id integer, nome text not null, email text, primary key(id))''')

c.execute('''INSERT INTO info VALUES
            (1902448, 'LUIS DIELLE', 'luis.dielle@hasl.com')''')

c.execute('''SELECT * FROM info''')

for row in c.fetchall():
    print(row)


conn.commit()
conn.close() 