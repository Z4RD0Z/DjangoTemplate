from django.test import TestCase, SimpleTestCase


# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')