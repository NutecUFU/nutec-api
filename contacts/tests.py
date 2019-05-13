from django.test import TestCase, Client


class ContactTest(TestCase):

    def setUp(self):
        self.path = "/v1/contacts/"
        self.client = Client()
        self.contact = {
            'name': "Mathews",
            'email': "mathews@gmail.com",
            'message': "Test Message",
            'date': "2019-05-13T10:20:00Z"
        }

    def test_create_contact(self):
        """ should create a contact """

        response = self.client.post(self.path, self.contact)

        self.assertEqual(response.status_code, 201)

    def test_get_contacts(self):
        """ should get a contact """
        self.client.post(self.path, self.contact)

        response = self.client.get(self.path)
        res = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['results'], [self.contact])

    def test_remove_contacts(self):
        """ should receive 401 response """
        self.client.post(self.path, self.contact)
        test_path = self.path + '1/'

        response = self.client.delete(test_path)

        self.assertEqual(response.status_code, 401)

    def test_update_contacts(self):
        """ should receive 401 response """
        self.client.post(self.path, self.contact)
        test_path = self.path + '1/'

        response = self.client.put(test_path)

        self.assertEqual(response.status_code, 401)
