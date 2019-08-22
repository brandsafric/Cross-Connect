from django.test import TestCase, Client
from users.tests.test_models import CustomUserTestCase
from church.tests.test_models import ChurchTestCase
from crossconnect.tests import GlobalTestCase

class TestChurchURLs(TestCase):
    def setUp(self):
        church_test_case = ChurchTestCase()
        church = church_test_case.create_church()
        user_test_case = CustomUserTestCase()
        user = user_test_case.create_user()
        user.home_church = church
        user.save()
        self.client.force_login(user)


    def test_add_church(self):
        form_data = {
            'name': 'Test',
            'city': 'place',
            'state': 'large place'
        }

        request = self.client.get('/app/church/add')
        response = self.client.post('/app/church/add', form_data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response.status_code, 302)

    def test_add_service_template(self):
        form_data = {
            'name': 'Service A',
            'time': '08:00:00',
            'day': 6
        }
<<<<<<< Updated upstream
        request = self.client.get('/app/church/services/add')
        response = self.client.post('/app/church/services/add', form_data)
=======


        request = self.client.get('/app/church/services/templates/add')
        response = self.client.post('/app/church/services/templates/add', form_data)
>>>>>>> Stashed changes
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response.status_code, 302)
