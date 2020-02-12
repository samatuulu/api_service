from rest_framework import status
# from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ExampleTestCase(APITestCase):
    def test_url_root(self):
        url = "http://localhost:5000/api/tasks/"
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))


class ExampleTestCase2(APITestCase):
    def test_url_root(self):
        url = "http://localhost:5000/api/tags/"
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))