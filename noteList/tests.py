from django.test import TestCase

class Home_Test(TestCase):
    def test_home_return_html(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

