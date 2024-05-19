from api.v1.app import app
import unittest

'''test the flask api route'''

class Test_api_valid_route(unittest.TestCase):
    '''test the routes defined in the api route'''
    def setUp(self):
        '''setup test client'''
        self.app = app.test_client()

    def test_status_route(self):
        '''test the status route'''
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "OK"})


    def test_nonexisting_route(self):
        '''test nonexisting route'''
        response = self.app.get('/api/v1/nonexisting')
        self.assertEqual(response.status_code, 404)
