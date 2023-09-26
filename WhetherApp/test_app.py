import json
import unittest
from flask import Flask
from app import app

class WeatherViewTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_city(self):
        response = self.app.get('/weather/San%20Francisco')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['temperature'], 14)
        self.assertEqual(data['weather'], 'Cloudy')

    def test_invalid_city(self):
        response = self.app.get('/weather/InvalidCity')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
