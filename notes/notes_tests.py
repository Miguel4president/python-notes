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

    def test_get_all(self):
        token_header = {"myToken": "This can be anything"}

        response = self.app.get('/api/v1/tenants/1/notes', headers=token_header)
        assert response.data


if __name__ == '__main__':
    unittest.main()
