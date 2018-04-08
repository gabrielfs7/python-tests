import sqlite3
import os


class Database:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        db_path = os.path.dirname(os.path.realpath(__file__)) + "/sqlite.db"

        self.connection = sqlite3.connect(db_path)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
        )
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",
            (title, author, year, isbn, id)
        )
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO books(id, title, author, year, isbn) VALUES(NULL, ?, ?, ?, ?)",
            (title, author, year, isbn)
        )
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (id, ))

        self.connection.commit()

    def select(self, id="", title="", author="", year="", isbn=""):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM books WHERE id LIKE ? AND title LIKE ? AND author LIKE ? AND year LIKE ? AND isbn LIKE ?",
            ("%" + id + "%", "%" + title + "%", "%" + author + "%", "%" + year + "%", "%" + isbn + "%")
        )

        return cursor.fetchall()