"""

This is an example how to integrate Postgres database to python scripts

"""
import psycopg2

host = '127.0.0.1'
port = 5432
db = 'store'
user = 'postgres'
passwd = 'root'

connection = psycopg2.connect("dbname='" + db + "' user='" + user + "' password='" + passwd + "' host='" + host + "'")


def create_table():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER, item TEXT, quantity INTEGER, price REAL)")
    connection.commit()


def update(id, item, quantity, price):
    cursor = connection.cursor()
    cursor.execute("UPDATE product SET item = %s, quantity = %s, price = %s WHERE id = %s", (item, quantity, price, id))
    connection.commit()


def insert(id, item, quantity, price):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM product WHERE id = %s", (id, ))

    result = cursor.fetchone()

    if result is not None:
        return update(id, item, quantity, price)

    cursor = connection.cursor()
    cursor.execute("INSERT INTO product VALUES(%s, %s, %s, %s)", (id, item, quantity, price))
    connection.commit()


def delete(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM product WHERE id = %s", (id, ))
    connection.commit()


def select():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM product")

    return cursor.fetchall()


create_table()
insert(1, 'Book DDD', 1, 20.99)
insert(2, 'Book Clean code', 1, 21.99)
insert(3, 'Book Clean coder', 1, 25.69)

print(select())

delete(2)
update(3, 'Book Clean coder - New Edition', 2, 26.89)

print(select())

connection.close()