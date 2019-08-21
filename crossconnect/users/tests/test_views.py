from django.test import TestCase
from django.urls import reverse
from users.views import *


class UsersViewsTestCase(TestCase):
    def test_add_user_view(self):
        response = self.client.get(reverse('add_user'))
        self.assertTemplateUsed(template_name='add_user.html')
