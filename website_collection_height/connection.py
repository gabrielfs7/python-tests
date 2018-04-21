"""

This is an example how to integrate Postgres database to python scripts

"""
import psycopg2


class Connection():
    def __init__(self):
        host = '127.0.0.1'
        port = 5432
        db = 'store'
        user = 'postgres'
        passwd = 'root'
        self.__connection = psycopg2.connect("dbname='" + db + "' user='" + user + "' password='" + passwd + "' host='" + host + "'")

    def create_table(self):
        cursor = self.__connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER, item TEXT, quantity INTEGER, price REAL)")
        self.__connection.commit()

    def update(self, id, item, quantity, price):
        cursor = self.__connection.cursor()
        cursor.execute("UPDATE product SET item = %s, quantity = %s, price = %s WHERE id = %s", (item, quantity, price, id))
        self.__connection.commit()

    def insert(self, id, item, quantity, price):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT id FROM product WHERE id = %s", (id, ))

        result = cursor.fetchone()

        if result is not None:
            return self.update(id, item, quantity, price)

        cursor = self.__connection.cursor()
        cursor.execute("INSERT INTO product VALUES(%s, %s, %s, %s)", (id, item, quantity, price))
        self.__connection.commit()

    def delete(self, id):
        cursor = self.__connection.cursor()
        cursor.execute("DELETE FROM product WHERE id = %s", (id, ))
        self.__connection.commit()

    def select(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM product")

        return cursor.fetchall()

    def close(self):
        self.__connection.close()
