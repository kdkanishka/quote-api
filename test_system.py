import unittest
import requests

BASE_URL = 'http://localhost:5000'  # Update the URL if necessary

class TestSystem(unittest.TestCase):
    def test_get_quote(self):
        response = requests.get(f'{BASE_URL}/quote')
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', data)

if __name__ == '__main__':
    unittest.main()
