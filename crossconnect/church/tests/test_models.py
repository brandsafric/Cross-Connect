from django.test import TestCase
from church.models import Church, ServiceTemplate

class ChurchTestCase(TestCase):

    def _create_church(self):
        data_dict = {
            'name':'Test Church',
            'city': 'Redlands',
            'state': 'California'
        }
        return Church.objects.create(**data_dict)

    def _create_service_template(self, church):
        data_dict = {
            'church': church,
            'name': 'Service A',
            'time': "08:00:00",
            'day': 0
        }
        return ServiceTemplate.objects.create(**data_dict)

    def test_create_church(self):
        church = self._create_church()
        self.assertEqual(church.pk, church.id)

    def test_create_service_template(self):
        church = self._create_church()
        service = self._create_service_template(church)
        self.assertEqual(service.pk, service.id)
