from django.test import TestCase
from church.models import Church

class ChurchTestCase(TestCase):

    def test_create_church(self):
        """
        Tests whether Church model is functional
        """
        data_dict = {
            'name':'Test Church',
            'city': 'Redlands',
            'state': 'California'
        }
        church = Church.objects.create(**data_dict)
        self.assertEqual(church.pk, church.id)
