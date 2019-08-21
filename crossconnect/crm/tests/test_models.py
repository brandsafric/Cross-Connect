# from django.test import TestCase
# from church.models import Contact, ServiceTemplate
#
# class CrmModelsTestCase(TestCase):
#
#     def create_contact(self):
#         data_dict = {
#             'name':'Test Church',
#             'city': 'Redlands',
#             'state': 'California'
#         }
#         return Church.objects.create(**data_dict)
#
#
#     def test_create_church(self):
#         church = self.create_church()
#         self.assertEqual(church.pk, church.id)
#
#     def test_create_service_template(self):
#         church = self.create_church()
#         service = self.create_service_template(church)
#         self.assertEqual(service.pk, service.id)
