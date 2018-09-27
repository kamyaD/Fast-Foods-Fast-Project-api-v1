# import json
# import unittest
# import os
# from app.views.views import app


# os.sys.path.append("../")


# class ApiEndpoints(unittest.TestCase):


#     # Ensure All orders orders are returned
#     def test_returnAll(self):
#         client = app.test_client(self)
#         output = client.get(
#             '/api/v1/orders_all', content_type='application/json')
#         self.assertEqual(output.status_code, 200)


#     # Ensure that new order is created
#     def test_addOrder(self):
#         client = app.test_client(self)
#         self.order= {
#             "id": 1,
#             "name": "coffe",
#             "price": 89
#         }
#         output = client.post(
#             '/api/v1/orders_post', data = json.dumps(self.order), content_type="application/json")
#         response = client.get("/api/v1/orders_get/1", content_type="application/json")
#         self.assertTrue(output.status_code, 201 )
       

#     # Ensure status of an order is Updated
#     def test_editOrder(self):
#         client = app.test_client(self)
#         self.new_orders={
#             "id": 1,
#             "name": "Milk",
#             "price": 100
#         }
#         self.old_edit= {
#             "id": 1,
#             "name": "bread",
#             "price": 200
#         }
#         posted = client.post("/api/v1/orders_post", data=json.dumps(self.old_edit), content_type="application/json")
#         output = client.put(
#             '/api/v1/orders_put/1' , data = json.dumps(self.new_orders), content_type="application/json")
#         resp = client.get("/api/v1/orders_get/1", content_type="application/json")
#         # print(resp.data)
#         self.assertEqual(json.loads(resp.data), self.new_orders)
#         self.assertEqual(resp.status_code, 200)


#     # Ensure  an order is deleted

#     def test_deleteOrder(self):
#         client = app.test_client(self)
#         # print(res.data)
#         output = client.delete(
#             '/api/v1/orders_del/1' , content_type="application/json")
#         res = client.get("/api/v1/orders_all", content_type="application/json")
#         self.assertNotEqual(res.data, 'orders: []')
#         self.assertTrue(output.status_code, 201)
#         # print(output.data)
#         # self.assertEqual(1,2)
#         # self.assertNotIn(self.orders, self.new_orders)






# if __name__ == '__main__':
#     unittest.main()
