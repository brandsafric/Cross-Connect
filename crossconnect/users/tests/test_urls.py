from django.test import TestCase, Client

class TestUsersURLs(TestCase):

    def test_register(self):
        """
        Tests whether register url is functional
        """
        response = self.client.get('/user/register')
        self.assertEqual(response.status_code, 200)
