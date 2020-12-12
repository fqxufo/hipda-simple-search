import sqlite3

conn = sqlite3.connect('titles.db')
c = conn.cursor()
c.execute('''CREATE TABLE titles
       (title           TEXT    NOT NULL,
       tid            TEXT     NOT NULL,
       postdate      TEXT   NOT NULL,
       PRIMARY KEY(tid));''')
conn.commit()
conn.close()