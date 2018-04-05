import sqlite3

conn = sqlite3.connect("books.db")


def create_table():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()


def insert(item, quantity, price):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()


def select():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")

    return cursor.fetchall()


create_table()
insert('DDD Book', 1, 20.99)
insert('Clean code', 1, 21.99)

print(select())

conn.close()
