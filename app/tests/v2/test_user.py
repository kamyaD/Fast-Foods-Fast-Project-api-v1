

#from app.api.v2.models.connection import MyDatabase
import unittest
import os
import json
from app import create_app

class orders(unittest.TestCase):
    """This class represents the orders test case"""

    def setUp(self):
        self.app = create_app(config_name="test")
        self.client = self.app.test_client()
        self.orders = {
 	    "order_name": "Sambusa",
        "customer_name": "Domnic"     
        }

        self.user = dict(
            name="kamya",
            email="domisemak@yahoo.co.uk",
            password="newpass"        
        )

        self.menu = {
            "food_name": "Fish",
            "food_desc": "Nice Meal",
            "food_price": 800
        }

    
    def token_content(self):
        response=self.client.post('api/v2/login', content_type='application/json', data=json.dumps(self.user))
        token = json.loads(response.data.decode("utf-8"))["data"]["token"]
        return token
    
    def test_login(self):
        response= self.client.post('/api/v2/login', content_type='application/json', data=json.dumps(self.user))
        self.assertEqual(response.status_code,200)
                  
    def test_userRegister(self):
        response=self.client.post('/api/v2/user', content_type='application/json', data=json.dumps(self.user))
        self.assertEqual(response.status_code,201)
    
    def test_addOrder(self):
        token = self.token_content()
        response=self.client.post('/api/v2/orders', headers=dict(Authorization="Bearer " + token), content_type='application/json', data=json.dumps(self.orders))
        self.assertEqual(response.status_code,200)
    
    def test_createMenu(self):
        token = self.token_content()
        response=self.client.post('/api/v2/menu', headers=dict(Authorization="Bearer " + token), content_type='application/json', data=json.dumps(self.menu))
        self.assertEqual(response.status_code,200)
     
    def test_userHistry(self):
        response=self.client.get('/api/v2/orders/Domnic', content_type='application/json', data=json.dumps(self.orders))
        self.assertEqual(response.status_code,200)
    
    def test_return_menu(self):
        response=self.client.get('/api/v2/orders/menu', content_type='application/json')
        self.assertEqual(response.status_code,200)
    
    def test_orderById(self):
        token = self.token_content()
        self.client.post('/api/v2/orders', headers=dict(Authorization="Bearer " + token), content_type='application/json', data=json.dumps(self.orders))
        response=self.client.get('/api/v2/orders/1',headers=dict(Authorization="Bearer " + token), content_type='application/json')
        self.assertEqual(response.status_code,200)
    








    
    

