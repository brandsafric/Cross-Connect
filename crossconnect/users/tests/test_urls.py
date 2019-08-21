from django.test import TestCase, Client

class TestUsersURLs(TestCase):

    def test_register_user(self):
        """
        Tests whether users urls are functional
        """

        form_data = {
            'first_name': 'Joe',
            'last_name': 'Schmow',
            'email': 'joe@gmail.com',
            'password1': 'password123',
            'password2': 'password123'
        }

        request = self.client.get('/user/register')
        response = self.client.post('/user/register', form_data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response.status_code, 302)
