import unittest
from api.routes import api_bp
from flask import Flask


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api_bp)

        self.client = self.app.test_client()

    def test_get_quote(self):
        response = self.client.get('/quote')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', data)


if __name__ == '__main__':
    unittest.main()
