import sqlite3
import os


class Database():
    def __init__(self):
        current_dir = os.getcwd()
        db_name = 'become_qa_auto.db'

        self.connection = sqlite3.connect(os.path.join(current_dir, db_name))

        self.cursor = self.connection.cursor()

        # set the usual test id
        self.test_id = 999

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"

        self.cursor.execute(sqlite_select_Query)

        record = self.cursor.fetchall()

        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        return record

    def get_all_products(self):
        query = "SELECT * FROM products"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers \
            WHERE name = '{name}'"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} \
            WHERE id = {product_id}"

        self.cursor.execute(query)

        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT INTO products \
            (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"

        self.cursor.execute(query)

        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"

        self.cursor.execute(query)

        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        return record

    def get_product(self, product_id):
        query = f"SELECT * FROM products WHERE id = {product_id}"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        return record

    def auto_add_id(self, name, description, qnt):
        query = f"INSERT INTO products \
            (name, description, quantity) \
            VALUES ('{name}', '{description}', {qnt})"

        self.cursor.execute(query)

        self.connection.commit()

    def null_values(self, qnt):
        query = f"INSERT INTO products (quantity) VALUES ({qnt})"

        self.cursor.execute(query)

        self.connection.commit()

    # TOOLBOX
    # for cursom queries
    def hammer(self, query):
        self.cursor.execute(query)

        self.connection.commit()
        record = self.cursor.fetchall()

        return record
