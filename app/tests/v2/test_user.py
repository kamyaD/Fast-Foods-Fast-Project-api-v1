from app.tests.v2.test_config import app
from app.api.v2.models.connection import MyDatabase
import unittest

class UserRegistration(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client(self)
        MyDatabase.create_test_db()
        
        self.database = MyDatabase()
        self.database.create_orders()
        self.database.create_users()
        self.database.create_menu()
    
    # Testing User registration   
    def test_user_details(self):
        
        output = self.client.post('/api/v2/user_register', data=dict(
            name = "Domnic", email = "domisemak@yahoo.com",
            pw= "admin", confirm_pw = "admin"
        ), follow_redirects=True )
        
        self.assertEqual(output.status_code, 200)


    # Testing user login 
    def test_user_login(self):
        output = self.client.post('/user_login', data=dict(user_name="domnic", pw="dommy1"),
        follow_redirects=True)
        self.assertIn(b'You are now logged in, Please make your order',output.data)

    # Testing user log out
    def test_user_logout(self):
        self.client.post('/user_login', data=dict(user_name="domnic", pw="dommy1"),
        follow_redirects=True)
        output = client.get('/user_logout', follow_redirects=True)
        self.assertIn(b'Thank you, you are now loged out!',output.data)
        self.assertEqual(output.status_code, 200) 

    # Testing placing an order
    def test_place_order(self):
        order= {
            "id": 1,
            "name": "coffe",
            "price": 89
        }

        output = self.client.post(
            '/order', data = json.loads(order), content_type="application/objects")
        response = client.get("order/1", content_type="application/objects")
        self.assertTrue(output.status_code, 201 )

    # Testing Get all orders
    def test_get_all_orders(self):
        output = self.client.get(
            '/orders', content_type='application/json')
        self.assertEqual(output.status_code, 200)

    
    # Add a specific Order
    def test_addOrder(self):
        order= {
            "id": 1,
            "name": "coffe",
            "price": 89
        }
        output = self.client.post(
            '/order/1', data = json.dumps(order), content_type="application/json")
        response = client.get("/order1", content_type="application/json")
        self.assertTrue(output.status_code, 201 )
       

    # Get available Menu
    def test_get_all_menu(self):
        output = self.client.get(
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

        posted = self.client.post(
            "/order", 
            data=json.dumps(self.old_edit), 
            content_type="application/json")

        output = client.put(
            '/order/1' , data = json.dumps(self.new_orders), content_type="application/json")
        resp = client.get("/order/1", content_type="application/json")
        # print(resp.data)
        self.assertEqual(json.loads(resp.data), self.new_orders)
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        self.database.teardown()