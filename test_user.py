import unittest
from flask import Flask

import psycopg2
app = Flask(__name__)



class UserRegistration(unittest.TestCase):
    
    # Testing User registration   
    def test_user_details(self):
        client = app.test_client(self)
        output = client.post('/user_register', data=dict(
            name = "Domnic", email = "domisemak@yahoo.com",
            pw= "admin", confirm_pw = "admin"
        ), follow_redirects=True )
        
        self.assertEqual(output.status_code, 200)


    # Testing user login 
    def test_user_login(self):
        client = app.test_client(self)
        output = client.post('/user_login', data=dict(user_name="domnic", pw="dommy1"),
        follow_redirects=True)
        self.assertIn(b'You are now logged in, Please make your order',output.data)

    # Testing user log out
    def test_user_logout(self):
        client = app.test_client(self)
        client.post('/user_login', data=dict(user_name="domnic", pw="dommy1"),
        follow_redirects=True)
        output = client.get('/user_logout', follow_redirects=True)
        self.assertIn(b'Thank you, you are now loged out!',output.data)
        self.assertEqual(output.status_code, 200) 

    # Testing placing an order
    def test_place_order(self):
        client = app.test_client(self)
        self.order= {
            "id": 1,
            "name": "coffe",
            "price": 89
        }
        output = client.post(
            '/order', data = json.loads(self.order), content_type="application/objects")
        response = client.get("order/1", content_type="application/objects")
        self.assertTrue(output.status_code, 201 )

    # Testing Get all orders
    def test_get_all_orders(self):
        client = app.test_client(self)
        output = client.get(
            '/orders', content_type='application/json')
        self.assertEqual(output.status_code, 200)

    
    # Add a specific Order
    def test_addOrder(self):
        client = app.test_client(self)
        self.order= {
            "id": 1,
            "name": "coffe",
            "price": 89
        }
        output = client.post(
            '/order/1', data = json.dumps(self.order), content_type="application/json")
        response = client.get("/order1", content_type="application/json")
        self.assertTrue(output.status_code, 201 )
       

    # Get available Menu
    def test_get_all_menu(self):
        client = app.test_client(self)
        output = client.get(
            '/menu', content_type='application/json')
        self.assertEqual(output.status_code, 200)

    # Testing add a meal option
    def test_editOrder(self):
        client = app.test_client(self)
        self.meals={
            "id": 1,
            "name": "Milk",
            "price": 100
        }
        self.meals_edit= {
            "id": 1,
            "name": "bread",
            "price": 200
        }
        posted = client.post("/order", data=json.dumps(self.old_edit), content_type="application/json")
        output = client.put(
            '/order/1' , data = json.dumps(self.new_orders), content_type="application/json")
        resp = client.get("/order/1", content_type="application/json")
        # print(resp.data)
        self.assertEqual(json.loads(resp.data), self.new_orders)
        self.assertEqual(resp.status_code, 200)






    # Add a meal option to the menu




    
    


    
    






