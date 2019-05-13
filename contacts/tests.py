from django.test import TestCase, Client


class ContactTest(TestCase):

    def setUp(self):
        self.path = "/v1/contacts/"
        self.client = Client()

    def test_create_contact(self):
        """ should create a contact """

        contact = {'name': "Mathews", 'email': "mathews@gmail.com", 'message': "Test Message"}

        response = self.client.post(self.path, contact)

        self.assertEqual(response.status_code, 201)

    def test_get_contacts(self):
        """ should get a contact """
        contact = {'name': "Mathews", 'email': "mathews@gmail.com", 'message': "Test Message"}
        self.client.post(self.path, contact)

        response = self.client.get(self.path)
        res = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['results'][0], contact)
