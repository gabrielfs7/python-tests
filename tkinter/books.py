import sqlite3

conn = sqlite3.connect("books.db")


def create_table():
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
    )
    conn.commit()


def update(id, title, author, year, isbn):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",
        (title, author, year, isbn, id)
    )
    conn.commit()


def insert(id, title, author, year, isbn):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM books WHERE id = ?", (id, ))

    result = cursor.fetchone()

    if result is not None:
        return update(id, title, author, year, isbn)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?)", (id, title, author, year, isbn))
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
insert(1, 'DDD', 'Author', 2000, 1234)
insert(2, 'Clean code', 'Author', 2001, 12345)
insert(3, 'Clean coder', 'Author', 2010, 123456)

print(select())

delete(2)
update(3, 'Clean coder - New Edition', 'Author', 2010, 123456)

print(select())

conn.close()
