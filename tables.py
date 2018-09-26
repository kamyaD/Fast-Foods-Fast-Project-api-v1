import psycopg2
from pprint import pprint
import sys


table1= "CREATE TABLE IF NOT EXISTS vendors(vendor_id SERIAL PRIMARY KEY,vendor_name VARCHAR(255) NOT NULL)"
name= ("7", "java Kangethe")
table1_insert= "INSERT INTO  vendors(vendor_id,vendor_name) VALUES('"+name[0]+"','"+name[1]+"')"
table_dt_delete= "DELETE FROM vendors WHERE vendor_id = 4"
edit_table = "UPDATE vendors SET vendor_id=2 WHERE vendor_id=3"


