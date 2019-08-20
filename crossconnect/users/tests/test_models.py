from django.test import TestCase
from django.contrib.auth import get_user_model
from users.forms import CustomUserCreationForm

User = get_user_model()

class CustomUserTestCase(TestCase):

    def test_create_user(self):
        """
        Tests whether customuser model is functional
        """
        data_dict = {
            'email':'test@email.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_pastor': 'True'
        }
        user = User.objects.create(**data_dict)
        self.assertEqual(user.pk, user.id)
