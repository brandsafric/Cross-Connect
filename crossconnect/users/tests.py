from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class CustomUserTestCase(TestCase):

    def test_create_user(self):
        data_dict = {
            'email':'test@email.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_pastor': 'True'
        }
        user = User.objects.create(**data_dict)
        self.assertEqual(user.pk, user.id)
