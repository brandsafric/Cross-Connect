from django.test import TestCase, Client
from django.urls import reverse
from users.views import *


class ChurchViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_add_church_view(self):
        response = self.client.get(reverse('add_church'))
        self.assertTemplateUsed(response, 'church/add_church.html')
