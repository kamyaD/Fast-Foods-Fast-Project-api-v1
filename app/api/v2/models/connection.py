import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from flask import jsonify
import sys
from datetime import datetime
import os
from instance.config import app_config


class MyDatabase:

    def __init__(self):
        self.connection_rout = app_config[os.getenv('APP_ENV')].DATABASE_URL
        self.connection = psycopg2.connect(self.connection_rout)

    # creating user registration table
    def create_user(self):
        table1 = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, name VARCHAR(25),email VARCHAR, password VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table1)
        self.connection.commit()

    @classmethod
    def create_test_db(cls):

        try:
            connection_rout = app_config[os.getenv(
                'APP_ENV')].DATABASE_CREATE_URL
            connection = psycopg2.connect(connection_rout)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE {}".format(
                app_config[os.getenv('APP_ENV')].DB_NAME))
            connection.commit()

            return True
        except BaseException:
            return False

    # create menu
    def create_menu(self):
        self.connection
        menu = "CREATE TABLE IF NOT EXISTS menu(food_id SERIAL NOT NULL PRIMARY KEY, food_name VARCHAR(25),food_desc VARCHAR (25), food_price INT)"
        cursor = self.connection.cursor()
        cursor.execute(menu)
        self.connection.commit()

    # creating Orders table
    def create_orders(self):
        self.connection_rout
        self.connection
        table2 = "CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,order_date DATE,customer_name VARCHAR(25) NOT NULL,order_name VARCHAR(25)," \
                 " order_status VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table2)
        self.connection.commit()

    def teardown(self):
        table2 = "DROP ALL TABLES"
        cursor = self.connection.cursor()
        cursor.execute(table2)
        self.connection.commit()


class Orders(MyDatabase):

    def __init__(self, order_name=None, customer_name=None):
        super().__init__()
        self.order_name = order_name
        self.order_status = "pending"
        self.customer_name = customer_name
        self.date = datetime.now()

    def serialize(self):
        return dict(
            id=self.id,
            name=self.order_name,
            orderd_by=self.customer_name,
            status=self.order_status,
            date=str(self.date)
        )

    def place_order(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM menu WHERE food_name='{}'".format(self.order_name))
        menu = cursor.fetchone()
        print(menu)

        if not menu:
            return jsonify(
                {"message": "The food item you ordered does not exist in our menu"})

        cursor.execute("INSERT INTO  orders(order_name, order_status, customer_name, order_date) VALUES(%s,%s,%s,%s)",
                       (self.order_name, self.order_status, self.customer_name, self.date))
        self.connection.commit()

    def map_object(self, convert):
        order = Orders(order_name=convert[3], customer_name=convert[2])
        order.id = convert[0]
        order.date = convert[1]
        order.order_status = convert[4]

        return order

    def all_orders(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        self.connection.commit()
        orders = cursor.fetchall()

        if orders:
            return [self.map_object(order) for order in orders]

        # Get a specific order:

    def get_specific_order(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id=%s", (id,))
        order = cursor.fetchone()
        self.connection.commit()

        if order:
            return self.map_object(order)

    def update_order_status(self):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE orders SET order_status = '%s' WHERE order_id = %s " %
                       (self.order_status, self.id))

        self.connection.commit()
        return True

    def get_user_order_histry(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM orders WHERE customer_name = '%s' " %
            (self.customer_name))

        orders = cursor.fetchall()
        self.connection.commit()

        return orders


class User(MyDatabase):

    def __init__(self, name="", email="", password=""):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password

    def insert_to_user(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES ('%s' , '%s', '%s')
            """ % (self.name, self.email, self.password))

        self.connection.commit()

    def map_object(self, convert):
        self.id = convert[0]
        self.name = convert[1]
        self.email = convert[2]
        self.password = convert[3]

        return self

    def get_user_by_name(self, name):
        print("name", name)
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name='%s'" % (name))
        user = cursor.fetchone()
        print(user)
        if user:
            return self.map_object(user)

    def get_user_by_id(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users where id=%s" (id,))
        user = cursor.fetchone()

        self.connection.commit()

        if user:
            return self.map_object(user)


class Menu(MyDatabase):

    def __init__(self, food_name=None, food_desc=None, food_price=None):
        super().__init__()
        self.food_name = food_name
        self.food_desc = food_desc
        self.food_price = food_price

    def insert_to_menu(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO menu (food_name, food_desc, food_price)
            VALUES (%s , %s, %s)
            """,
                       (self.food_name, self.food_desc, self.food_price))

        self.connection.commit()

    def map_object(self, convert):

        food = Menu(
            food_name=convert[1],
            food_desc=convert[2],
            food_price=convert[3])
        food.id = convert[0]

        self = food
        return self

    def all_menu(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM menu")
        foods = cursor.fetchall()
        self.connection.commit()

        if foods:
            return [self.map_object(food) for food in foods]

    def get_food_by_id(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM menu WHERE id=%s", (id, ))

        food = cursor.fetchone()

        if food:
            return self.map_object(food)

    def serialize(self):
        return dict(
            id=self.id,
            name=self.food_name,
            description=self.food_desc,
            price=self.food_price
        )