import os
import app
import unittest
import tempfile
from base64 import b64encode


class NotesTestCase(unittest.TestCase):

    # Happens before EVERY test case
    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    # Happens after EVERY test case
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def test_basic_auth_required(self):
        response = self.app.get('/api/v1/tenants')
        print response.status_code
        assert response.status_code == 401

    def test_basic_auth_with_invalid_creds(self):
        username = "admin"
        password = "FlubbedIt"

        headers = {
            'Authorization': 'Basic ' + b64encode("{0}:{1}".format(username, password))
        }

        response = self.app.get('/api/v1/tenants', headers=headers)
        assert response.status_code == 401

    def test_pass_basic_auth(self):
        username = "admin"
        password = "secret"

        headers = {
            'Authorization': 'Basic ' + b64encode("{0}:{1}".format(username, password))
        }

        response = self.app.get('/api/v1/tenants', headers=headers)
        assert response.status_code == 200

    def test_token_auth_required(self):
        response = self.app.get('/api/v1/tenants/1/notes')
        print response.status_code
        assert response.status_code == 401

    def test_token_auth_with_invalid_creds(self):
        key = "myToken"
        value = "this could be anything"

        headers = {
            key: value
        }

        response = self.app.get('/api/v1/tenants/1/notes', headers=headers)
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
