import psycopg2
from flask import jsonify
import sys
from datetime import datetime

class MyDatabase:

    def __init__(self):
        self.connection_rout = "host='localhost' dbname='orders' user='postgres' password='admin'"
        self.connection = psycopg2.connect(self.connection_rout)

    #creating user registration table
    def create_user(self):
        self.connection
        table1 = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, name VARCHAR(25), password VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table1)
        self.connection.commit()

        
    

    # create menu
    def create_menu(self):
        
        self.connection
        menu="CREATE TABLE IF NOT EXISTS MENU(food_id SERIAL NOT NULL PRIMARY KEY, food_item VARCHAR(25),food_description VARCHAR (25))"
        cursor = self.connection.cursor()
        cursor.execute(menu)
        self.connection.commit()

    #creating Orders table
    def  create_Orders(self):
    
        self.connection_rout
        self.connection
        table2 = "CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,order_date DATE,customer_name VARCHAR(25) NOT NULL,order_name VARCHAR(25)," \
                 " order_status VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table2)
        self.connection.commit()
    

class Orders(MyDatabase):

    def __init__(self, order_name = None, customer_name=None):
        super(Orders, self).__init__()
        self.order_name = order_name
        self.order_status = "pending"
        self.customer_name = customer_name
        self.date = datetime.now()

    def serialize(self):
        return dict(
            id=self.id,
            name=self.order_name,
            orderd_by=self.customer_name,
            status = self.order_status,
            date = str(self.date)
        )

    def place_order(self):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO  orders(order_name, order_status, customer_name, order_date) VALUES(%s,%s,%s,%s)",
                       (self.order_name, self.order_status, self.customer_name, self.date))
        self.connection.commit()


    def map_object(self, convert):
        self.id = convert[0]
        self.order_name = convert[1]
        self.order_status = convert[2]
        self.customer_name = convert[3]

        return self


    def all_orders(self):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM orders(order_status) VALUES()")
        self.connection.commit()
        orders = cursor.fetchall()


        if orders:
            return [self.map_object(order) for order in orders]


        # Get a specific order:

    def get_specific_order(self, id):
        self.connection

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = %s"(id,))
        order = cursor.fetchone()
        self.connection.commit()

        if order:
            return self.map_object(order)

    def update_order_status(self):
            self.connection
            cursor = self.connection.cursor()
            order=cursor.execute("INSERT INTO orders(order_status) VALUES(%S)"),
            (self.order_status)
            self.connection.commit()
        return order




class User(MyDatabase):

    def __init__(self, name, email, password):
        super(User, self).__init__()
        self.name = name
        self.email = email
        self.password = password


    def insert_to_menu(self):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (%s , %s, %s)
            """,
            (self.name, self.email, self.password))

        self.connection.commit()

    def map_object(self, convert):
        self.id = convert[0]
        self.name = convert[1]
        self.email = convert[2]
        self.password = convert[3]

        return self


    def get_user_by_name(self, name):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users where name=%s" (name,))

        user = cursor.fetchone()
        self.connection.commit()

        if user:
            return self.map_object(user)


        self.connection.commit()

    def get_user_by_id(self, id):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users where id=%s" (id,))
        user = cursor.fetchone()

        self.connection.commit()

        if user:
            return self.map_object(user)












class Menu(MyDatabase):

    def __init__(self, food_name, food_desc, food_price):
        super(Menu, self).__init__()
        self.food_name = food_name
        self.food_desc = food_desc
        self.food_price = food_price

    def insert_to_menu(self):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO menu (food_name, food_desc, food_price)
            VALUES (%s , %s, %s, %s)
            """,
            (self.food_name, self.food_desc, self.food_price))

        self.connection.commit()

    def all_menu(self):
        self.connection
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        self.connection.commit()


    

    
    
    
    
    
    
    












