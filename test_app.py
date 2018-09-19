import unittest

#local imports
from firstfood import orders
from firstfood import app 

class apiEndpoints(unittest.TestCase):
    
    
    # Ensure that flask is working
    def test_welcome(self):
        client = app.test_client(self)
        output = client.get('/v1', content_type='html/text')
        self.assertEqual(output.status_code, 200)
        self.assertIn(b'Welcome to Farst Foods Farst!.Please Sign up:', output.data)
    
    # Ensure All orders orders are returned
    def test_returnAll(self):
        client = app.test_client(self)
        output = client.get(
            '/api/v1/all_orders', content_type='html/text')
        self.assertEqual(output.status_code, 200)



if __name__ == '__main__':
    unittest.main()
