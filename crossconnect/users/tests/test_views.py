from django.test import TestCase
from django.urls import reverse
from users.views import *


class UsersViewsTestCase(TestCase):

    def test_register_get_view(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(template_name='register.html')
