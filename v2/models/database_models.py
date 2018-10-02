import os
import psycopg2

connection_rout = "host='localhost' dbname='orders' user='postgres' password='admin'"
connection = psycopg2.connect(connection_rout)
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user(user_id SERIAL NOT NULL PRIMARY KEY, " \
           "user_name VARCHAR(25),user_emailVARCHAR (25), user_pw VARCHAR (25)," \
           "confirm_pw varchar(25)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY," \
                      "customer_id varchar(25) NOT NULL," \
                      "order_name VARCHAR(25)," \
                 " order_status VARCHAR(25)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS menu(item_id SERIAL PRIMARY KEY," \
                      "item_name varchar(25) NOT NULL," \
                      "item_description VARCHAR(25)," \
                 " item_price VARCHAR(25)''')

