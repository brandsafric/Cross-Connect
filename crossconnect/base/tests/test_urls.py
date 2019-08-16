from django.test import TestCase, Client

# Create your tests here.



class TestBaseViews(TestCase):

    client = Client()

    def test_homepage(self):
        """
        Tests whether homepage is functional
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_styleguide(self):
        """
        Tests whether styleguide is functional
        """
        response = self.client.get('/styles/')
        self.assertEqual(response.status_code, 200)
