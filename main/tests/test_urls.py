import unittest
from django.test import Client
from main.views import primfacs


class TestUrls(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details_GET(self):
        # Issue a GET request.
        response = self.client.get('/test_task/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_details_POST(self):
        for num in range(1000):
            response = self.client.post('/test_task/', {'your_number': num})

            # Check that the rendered context contains 3 digits.
            self.assertEqual(response.context['result'], primfacs(num))
