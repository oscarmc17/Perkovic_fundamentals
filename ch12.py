import sqlite3

con = sqlite3.connect('web.db')

cur = con.cursor()

cur.execute("""CREATE TABLE Keywords 
            (Url text,
             word text,
             Freq int)
            )""")