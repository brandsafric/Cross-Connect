from django.test import TestCase, Client

class TestChurchURLs(TestCase):

    def test_add_church(self):
        """
        Tests whether church urls are functional
        """

        form_data = {
            'name': 'Test',
            'city': 'place',
            'state': 'large place'
        }

        request = self.client.get('/app/church/add')
        response = self.client.post('/app/church/add', form_data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response.status_code, 302)
