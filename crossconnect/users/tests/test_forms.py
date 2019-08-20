from django.test import TestCase
from users.forms import CustomUserCreationForm

class CustomUserForms(TestCase):

    def test_form(self):
        """
        Tests whether register form is functional
        """
        form_data = {
            'first_name': 'John_Test',
            'last_name': 'Doe_Test',
            'email': 'jdoe_test@gmail.com',
            'password1': 'passwordtest123',
            'password2': 'passwordtest123'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
