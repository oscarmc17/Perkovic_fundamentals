import sqlite3

con = sqlite3.connect('web.db')

cur = con.cursor()

cur.execute("""CREATE TABLE Keywords 
            (Url text,
             Word text,
             Freq int)""")

cur.execute("""INSERT INTO Keywords
            VALUES ('one.html', 'Beijing', 3)""")



url, word, freq = 'one.html', 'Paris', 5

cur.execute("""INSERT INTO Keywords
            VALUES (?, ?, ?)""", (url, word, freq))

record = ('one.html', 'Chicago', 5)

cur.execute("INSERT INTO Keywords VALUES (?, ?, ?)", record)

con.commit()
con.close()

# Practice Problem 12.3
def webData(db, url, links, freq):
    con = sqlite3.connect(db)
    cur = con.cursor()

    for word in freq:
        record = (url, word, freq[word])
        cur.execute("INSERT INTO Keywords VALUES (?,?,?)", record)
    for link in links:
        record = (url, link)
        cur.execute("INSERT INTO Keywords VALUES (?,?)", record) 
        
    con.commit()
    con.close()