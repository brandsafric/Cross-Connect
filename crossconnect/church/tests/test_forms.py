from django.test import TestCase
from church.forms import ChurchCreateForm

class ChurchForms(TestCase):

    def test_add_form(self):
        """
        Tests whether add form is functional
        """
        form_data = {
            'name': 'Church',
            'city': 'Place',
            'state': 'Larger place',
        }
        form = ChurchCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
