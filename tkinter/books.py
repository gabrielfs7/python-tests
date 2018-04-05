import sqlite3

conn = sqlite3.connect("books.db")


def create_table():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER, item TEXT, quantity INTEGER, price REAL)")
    conn.commit()


def update(id, item, quantity, price):
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET item = ?, quantity = ?, price = ? WHERE id = ?", (item, quantity, price, id))
    conn.commit()


def insert(id, item, quantity, price):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM books WHERE id = ?", (id, ))

    result = cursor.fetchone()

    if result is not None:
        return update(id, item, quantity, price)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?)", (id, item, quantity, price))
    conn.commit()


def delete(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id, ))
    conn.commit()


def select():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")

    return cursor.fetchall()


create_table()
insert(1, 'DDD Book', 1, 20.99)
insert(2, 'Clean code', 1, 21.99)
insert(3, 'Clean coder', 1, 25.69)

print(select())

delete(2)
update(3, 'Clean coder - New Edition', 2, 26.89)

print(select())

conn.close()
