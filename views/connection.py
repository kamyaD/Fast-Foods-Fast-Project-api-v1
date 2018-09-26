import psycopg2
import sys


#local imports
from tables import table1,table1_insert,table_dt_delete,edit_table


from pprint import pprint

class MyDatabase:
    connection_rout = "host='localhost' dbname='orders' user='postgres' password='admin'"
    connection = psycopg2.connect(connection_rout)


    def create_users(self):

        self.connection_rout
        self.connection
        table1 = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,user_name VARCHAR(25) " \
                 "NOT NULL,user_email VARCHAR(25), user_pw varchar(25), pw_confirm VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table1)
        self.connection.commit()

    def  create_Orders(self):
        self.connection_rout
        self.connection
        table2 = "CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,order_name VARCHAR(25)," \
                 " order_status VARCHAR(25))"
        cursor = self.connection.cursor()
        cursor.execute(table2)
        self.connection.commit()

    def place_order(self):
        self.connection_rout
        self.connection
        name = ("1", "java Kangethe", "open")
        insert1= "INSERT INTO  orders(order_id,order_name,order_status) VALUES('"+name[0]+"','"+name[1]+"','"+name[2]+"')"
        cursor = self.connection.cursor()
        cursor.execute(insert1)
        self.connection.commit()







        #cursor.execute(table1_insert)
        #cursor.execute(table_dt_delete)
        #cursor.execute(edit_table)
        #conn.commit()


    #def select(self):
    #     connection_rout = "host='localhost' dbname='orders' user='postgres' password='admin'"
    #     connection = psycopg2.connect(connection_rout)
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM vendors")
    #     orders = cursor.fetchall()
    #     for order in orders:
    #         pprint(order)
    #
    # def GetOne(self):
    #     connection_rout= "host='localhost' dbname='orders' user='postgres' password='admin'"
    #     connection = psycopg2.connect(connection_rout)
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM vendors WHERE vendor_id = %s", (1,))
    #     orders = cursor.fetchall()
    #     pprint(orders)
    #
    #
    #



if __name__=="__main__":
        #MyDatabase.create_users(MyDatabase)
        #MyDatabase.create_Orders(MyDatabase)
        # MyDatabase.GetOne(MyDatabase)
         MyDatabase.place_order(MyDatabase)

