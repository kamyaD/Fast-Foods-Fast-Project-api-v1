import json
import unittest
import os


# os.sys.path.append("../")
from app.views.views import app

class apiEndpoints(unittest.TestCase):


    # Ensure All orders orders are returned
    def test_returnAll(self):
        client = app.test_client(self)
        output = client.get(
            '/orders', content_type='application/json')
        self.assertEqual(output.status_code, 200)


    # Ensure that new order is created
    def test_addOrder(self):
        client = app.test_client(self)
        self.order= {
            "id": 1,
            "name": "coffe",
            "price": 89
        }
        output = client.post(
            '/orders', data = json.dumps(self.order), content_type="application/json")
        response = client.get("/orders/1", content_type="application/json")
        self.assertTrue(output.status_code, 201 )
        self.assertEqual(self.order, json.loads(response.data))

    # Ensure status of an order is Updated
    def test_editOrder(self):
        client = app.test_client(self)
        self.new_orders={
            "id": 1,
            "name": "Milk",
            "price": 100
        }
        self.old_edit= {
            "id": 1,
            "name": "bread",
            "price": 200
        }
        posted = client.post("/orders", data=json.dumps(self.old_edit), content_type="application/json")
        output = client.put(
            'orders/1' , data = json.dumps(self.new_orders), content_type="application/json")
        resp = client.get("orders/1", content_type="application/json")
        # print(resp.data)
        self.assertEqual(json.loads(resp.data), self.new_orders)
        self.assertEqual(resp.status_code, 200)


    # Ensure  an order is deleted

    def test_deleteOrder(self):
        client = app.test_client(self)
        # print(res.data)
        output = client.delete(
            '/orders' , content_type="application/json")
        res = client.get("/orders", content_type="application/json")
        self.assertNotEqual(res.data, 'orders: []')
        self.assertTrue(output.status_code, 201)
        # print(output.data)
        # self.assertEqual(1,2)
        # self.assertNotIn(self.orders, self.new_orders)






if __name__ == '__main__':
    unittest.main()
