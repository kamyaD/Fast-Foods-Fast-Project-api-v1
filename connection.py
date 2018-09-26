import psycopg2
import sys


#local imports
from tables import table1,table1_insert,table_dt_delete,edit_table


from pprint import pprint

class MyDatabase:
    def database(self):
        conn_string = "host='localhost' dbname='orders' user='postgres' password='admin'"
        connection = psycopg2.connect(conn_string)



        cursor = connection.cursor()
        cursor.execute(table1)
        cursor.execute(table1_insert)
        #cursor.execute(table_dt_delete)
        #cursor.execute(edit_table)
        conn.commit()
        print("connected!\n")

    def select(self):
        conn_string = "host='localhost' dbname='orders' user='postgres' password='admin'"
        connection = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vendors")
        orders = cursor.fetchall()
        for order in orders:
            pprint(order)

    def GetOne(self):
        conn_string = "host='localhost' dbname='orders' user='postgres' password='admin'"
        connection = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vendors WHERE vendor_id = %s", (1,))
        orders = cursor.fetchall()
        pprint(orders)






if __name__=="__main__":
        MyDatabase.database(MyDatabase)
        MyDatabase.select(MyDatabase)
        MyDatabase.GetOne(MyDatabase)

