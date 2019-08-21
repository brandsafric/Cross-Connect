from django.test import TestCase, Client
from users.tests.test_models import CustomUserTestCase
from church.tests.test_models import ChurchTestCase

class TestCrmURLs(TestCase):
    def setUp(self):
        church_test_case = ChurchTestCase()
        church = church_test_case.create_church()
        user_test_case = CustomUserTestCase()
        user = user_test_case.create_user()
        user.home_church = church
        user.save()
        self.client.force_login(user)


    def test_add_contact(self):
        form_data = {
            'first_name': 'Joe',
            'last_name': 'Schmow',
        }

        request = self.client.get('/app/contacts/add')
        response = self.client.post('/app/contacts/add', form_data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response.status_code, 302)

    
