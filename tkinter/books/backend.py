import sqlite3
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.dirname(os.path.realpath(__file__)) + "/sqlite.db"


connection = sqlite3.connect(db_path)


def create_table():
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
    )
    connection.commit()


def update(id, title, author, year, isbn):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",
        (title, author, year, isbn, id)
    )
    connection.commit()


def insert(title, author, year, isbn):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO books(id, title, author, year, isbn) VALUES(NULL, ?, ?, ?, ?)",
        (title, author, year, isbn)
    )
    connection.commit()


def delete(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id, ))
    connection.commit()


def select(id="", title="", author="", year="", isbn=""):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE id LIKE ? AND title LIKE ? AND author LIKE ? AND year LIKE ? AND isbn LIKE ?",
        ("%" + id + "%", "%" + title + "%", "%" + author + "%", "%" + year + "%", "%" + isbn + "%")
    )

    return cursor.fetchall()


create_table()

"""

Testing:

"""
# delete(1)
# delete(2)
# delete(3)

# print(select())

# insert(1, 'DDD', 'Author', 2000, 1234)
# insert(2, 'Clean code', 'Author', 2001, 12345)
# insert(3, 'Clean coder', 'Author', 2010, 123456)

# print(select())
# print(select(title="code"))

# delete(2)
# update(3, 'Clean coder - New Edition', 'Author', 2010, 123456)

# print(select())