import sqlite3
import os


class Database:
    def __init__(self):
        db_path = os.path.dirname(os.path.realpath(__file__)) + "/sqlite.db"

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS books " \
              "(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"

        self.cursor.execute(sql)
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        sql = "UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?"

        parameters = (
            title,
            author,
            year,
            isbn,
            id
        )

        self.cursor.execute(sql, parameters)
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        sql = "INSERT INTO books(id, title, author, year, isbn) VALUES(NULL, ?, ?, ?, ?)"

        parameters = (
            title,
            author,
            year,
            isbn
        )

        self.cursor.execute(sql, parameters)
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (id, ))
        self.connection.commit()

    def select(self, id="", title="", author="", year="", isbn=""):
        sql = "SELECT * FROM books WHERE " \
              "id LIKE ? AND title LIKE ? AND author LIKE ? AND year LIKE ? AND isbn LIKE ?"

        parameters = (
            "%" + id + "%",
            "%" + title + "%",
            "%" + author + "%",
            "%" + year + "%",
            "%" + isbn + "%"
        )

        self.cursor.execute(sql, parameters)

        return self.cursor.fetchall()