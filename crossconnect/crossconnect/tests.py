from django.test import TestCase
from model_mommy import mommy
from users.models import CustomUser
from church.models import Church, ServiceTemplate

class GlobalTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(CustomUser)
        self.church = mommy.make(Church)
        self.service_template = mommy.make(ServiceTemplate)

    def test_setup(self):
        self.assertEqual(self.user.pk, self.user.id)
        self.assertTrue(isinstance(self.user, CustomUser))

        self.assertEqual(self.church.pk, self.church.id)
        self.assertTrue(isinstance(self.church, Church))

        self.assertEqual(self.service_template.pk, self.service_template.id)
        self.assertTrue(isinstance(self.service_template, ServiceTemplate))
