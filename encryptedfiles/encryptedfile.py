from unittest import TestCase
from simplecrypt import encrypt, decrypt


class EncryptedFile(object):
    def __init__(self, path, password):
        self.__path = path
        self.__password = password

    def write(self, content, mode="w"):
        encrypted = encrypt(self.__password, content)
        with open(self.__path, mode) as fd:
            fd.write(encrypted)

    def read(self):
        with open(self.__path, "r") as fd:
            content = fd.read()
            return decrypt(self.__password, content)


class TestEncryptedFile(TestCase):

    def setUp(self):
        self.password = "password"
        self.path = "path_to_file.json"

    def test_write_and_read_same_content(self):
        content = "Hello World!"
        enc_file = EncryptedFile(self.path, self.password)
        enc_file.write(content)

        self.assertEqual(content, enc_file.read())

    def tearDown(self):
        import os
        if os.path.exists(self.path):
            os.remove(self.path)

