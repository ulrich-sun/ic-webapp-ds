import unittest
from app import app
import os

class FlaskAppTests(unittest.TestCase):

    # Set up the Flask testing client
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    # Test the main route
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # print(response.data)  # Print response data for debugging
        self.assertIn(b'IC GROUP', response.data)  # Check if title is present
        self.assertIn(b'Intranet &nbsp;Applications', response.data)  # Check if subtitle is present

    # Test with environment variables
    # TODO: check how to test with os (env vars) in python
    # def test_with_env_variables(self):
    #     os.environ['ODOO_URL'] = 'https://test-odoo.com'
    #     os.environ['PGADMIN_URL'] = 'https://test-pgadmin.com'

    #     response = self.app.get('/')
    #     self.assertEqual(response.status_code, 200)
    #     print(response.data)  # Print response data for debugging
    #     self.assertIn(b'https://test-odoo.com', response.data)  # Check if ODOO_URL is in the response
    #     self.assertIn(b'https://test-pgadmin.com', response.data)  # Check if PGADMIN_URL is in the response

    # Test without environment variables (should default to YouTube URLs in your app logic)
    def test_without_env_variables(self):
        if 'ODOO_URL' in os.environ:
            del os.environ['ODOO_URL']
        if 'PGADMIN_URL' in os.environ:
            del os.environ['PGADMIN_URL']

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://www.youtube.com/', response.data)  # Check if the default URL is used

if __name__ == '__main__':
    unittest.main()
