import sqlite3
# establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# query all data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# query certain columns
cursor.execute("SELECT band,date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()