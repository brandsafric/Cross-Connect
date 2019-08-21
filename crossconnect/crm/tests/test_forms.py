from django.test import TestCase
from church.forms import ChurchCreateForm, ServiceTemplateCreateForm

# class ChurchForms(TestCase):
#
#     def test_add_church_form(self):
#         form_data = {
#             'name': 'Church',
#             'city': 'Place',
#             'state': 'Larger place',
#         }
#         form = ChurchCreateForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_add_service_template_form(self):
#         form_data = {
#             'name': 'Service A',
#             'time': '08:00:00',
#             'day': 6,
#         }
#         form = ServiceTemplateCreateForm(data=form_data)
#         self.assertTrue(form.is_valid())
