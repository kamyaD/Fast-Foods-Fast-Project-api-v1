import psycopg2
from flask import jsonify
import sys



from pprint import pprint

class MyDatabase:
    connection_rout = "host='localhost' dbname='orders' user='postgres' password='admin'"
    connection = psycopg2.connect(connection_rout)
    

    
    # create user login
    def create_user(self):
        self.connection_rout
        self.connection
        login="CREATE TABLE IF NOT EXISTS login(user_id SERIAL NOT NULL PRIMARY KEY, user_name VARCHAR(25),user_pw VARCHAR (25))"
        cursor = self.connection.cursor()
        cursor.execute(login)
        self.connection.commit()
    
    def insert_to_login (self):
        self.connection_rout
        self.connection
        name = ("domnic","dommy1")
        login= "INSERT INTO  login(user_name,user_pw) VALUES('"+name[0]+"','"+name[1]+"')"
        cursor = self.connection.cursor()
        cursor.execute(login)
        self.connection.commit()
    
    
    # customer table
    def create_customers(self):
    
        self.connection_rout
        self.connection
        customer = "CREATE TABLE IF NOT EXISTS customer(customer_id INT NOT NULL PRIMARY KEY,customer_name VARCHAR(25) NOT NULL,phone_number VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(customer)
        self.connection.commit()
    
        # Registering customer:
    
    def register_customer (self):
    
        self.connection_rout
        self.connection
        name = ("20183", "Ken","0713747684")
        REG = "INSERT INTO  customer(customer_id,customer_name,phone_number) VALUES('" + name[0] + "','" + \
        name[1] + "','" + name[2] + "')"
        cursor = self.connection.cursor()
        cursor.execute(REG)
        self.connection.commit()
    
    #creating Orders table
    def  create_Orders(self):
    
        self.connection_rout
        self.connection
        table2 = "CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,order_date DATE,customer_id INT NOT NULL,order_name VARCHAR(25)," \
                 " order_status VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table2)
        self.connection.commit()
    
    # placing an order:
    def place_order(self, order_data):
        self.connection_rout
        self.connection
        name = order_data["name"]
        status = order_data["status"]
        insert1= "INSERT INTO  orders(order_name,order_status) VALUES(name,status)"
        cursor = self.connection.cursor()
        cursor.execute(insert1)
        self.connection.commit()
    
    # Get a list of orders:
    def all_orders(self):
        self.connection_rout
        self.connection
        all= "SELECT * FROM orders"
        cursor = self.connection.cursor()
        cursor.execute(all)
        self.connection.commit()
        orders = cursor.fetchall()
        return  jsonify(orders)

    # Get a specific order:
    def get_specific_order(self):
        self.connection_rout
        self.connection
        order= u"SELECT * FROM orders WHERE order_id = 1"
        cursor = self.connection.cursor()
        cursor.execute(order)
        self.connection.commit()
        orders = cursor.fetchall()
        for order in orders:
            pprint(order)
    
    # # Get order histry of a particular customer
    # def get_user_order(self):
    #     self.connection_rout
    #     self.connection
    #     histry="SELECT CAST(customer.customer_id AS INT),customer.customer_name FROM customer" \
    #            "orders.order_name,orders.order_date,orders.order_statues" \
    #            "FROM customer,orders" \
    #            "WHERE CAST(customer_id AS INT)= CAST(customer_id AS INT)"
    #     cursor = self.connection.cursor()
    #     cursor.execute(histry)
    #     self.connection.commit()
        orders = cursor.fetchall()
        for order in orders:
            pprint(histry)
    
    
    
    
    
    
    
    
    
    








if __name__=="__main__":
        #MyDatabase.create_user(MyDatabase)
        #MyDatabase.all_orders(MyDatabase)
        # MyDatabase.GetOne(MyDatabase)
         #MyDatabase.place_order(MyDatabase)
         #MyDatabase.all_orders(MyDatabase)
         #MyDatabase.update_order(MyDatabase)
        #MyDatabase.register_customer(MyDatabase)
         #MyDatabase.get_user_order(MyDatabase)
         MyDatabase.create_user(MyDatabase)





