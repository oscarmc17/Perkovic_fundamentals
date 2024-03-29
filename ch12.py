import sqlite3

# con = sqlite3.connect('web.db')

# cur = con.cursor()

# cur.execute("""CREATE TABLE Keywords
#             (Url text,
#              Word text,
#              Freq int)""")

# cur.execute("""INSERT INTO Keywords
#             VALUES ('one.html', 'Beijing', 3)""")


# url, word, freq = 'one.html', 'Paris', 5

# cur.execute("""INSERT INTO Keywords
#             VALUES (?, ?, ?)""", (url, word, freq))

# record = ('one.html', 'Chicago', 5)

# cur.execute("INSERT INTO Keywords VALUES (?, ?, ?)", record)

# con.commit()
# con.close()

# # Practice Problem 12.3
# def webData(db, url, links, freq):
#     con = sqlite3.connect(db)
#     cur = con.cursor()

#     for word in freq:
#         record = (url, word, freq[word])
#         cur.execute("INSERT INTO Keywords VALUES (?,?,?)", record)
#     for link in links:
#         record = (url, link)
#         cur.execute("INSERT INTO Keywords VALUES (?,?)", record)

#     con.commit()
#     con.close()


# LIST COMPREHENSION

# print([i for i in range(0, 20, 2)])
# print([len(word) for word in ['hawk', 'hen', 'hog', 'hyena']])

# PRACTICE PROBLEM 12.5
# words = ['hawk', 'hen', 'hog', 'hyena']
# print([word.capitalize() for word in words])
# print([(word, len(word)) for word in words])
# print([[(c, word) for c in word] for word in words])

# MAP REDUCE PROBLEM-SOLVING FRAMEKWORK
words = ['two', 'three', 'one', 'three', 'three', 'five', 'one', 'five']

def occurrence(word):
    'returns list containing tuple (word, 1)'
    return [(word, 1)]

intermediate1 = [occurrence(word) for word in words]
print(intermediate1)


def partition(intermediate1):
    dct = {}

    for lst in intermediate1:
        for key, value in lst:

            if key in dct:
                dct[key].append(value)
            else:
                dct[key] = [value]
    
    return dct.items()

intermediate2 = partition(intermediate1)
print(intermediate2)