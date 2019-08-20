from django.test import TestCase
from django.urls import reverse
from users.views import *


class UsersViewsTestCase(TestCase):

    def test_register_get_view(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(template_name='register.html')

    def test_register_post_view(self):

        form_data = {
            'first_name': 'John_Test',
            'last_name': 'Doe_Test',
            'email': 'jdoe_test@gmail.com',
            'password1': 'passwordtest123',
            'password2': 'passwordtest123'
        }

        response = self.client.post('/user/register', form_data)
        self.assertEqual(response.status_code, 302)
