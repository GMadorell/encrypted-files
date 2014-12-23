from unittest import TestCase
from encryptedfiles.encryptedfile import EncryptedFile
from encryptedfiles.encryptedjson import EncryptedJson
import os


class EncryptedFileTestCase(TestCase):
    def setUp(self):
        super(EncryptedFileTestCase, self).setUp()
        self.password = "password"
        self.path = "path_to_file.json"
        if not os.path.exists(self.path):
            with open(self.path, "a+"):
                pass
        self.enc_file = EncryptedFile(self.path, self.password)

    def tearDown(self):
        super(EncryptedFileTestCase, self).tearDown()
        if os.path.exists(self.path):
            os.remove(self.path)


class TestEncryptedFile(EncryptedFileTestCase):
    def test_read_unexisting_file_raise_ioerror(self):
        enc_file = EncryptedFile("some_file_that_does_not_exist", self.password)
        with self.assertRaises(IOError):
            enc_file.read()

    def test_read_empty_file(self):
        content = self.enc_file.read()
        self.assertEqual(content, "")

    def test_write_and_read_same_content(self):
        content = "Hello World!"
        self.enc_file.write(content)

        self.assertEqual(content, self.enc_file.read())


class TestEncryptedJson(EncryptedFileTestCase):
    def setUp(self):
        # Ensure a valid json file exists
        super(TestEncryptedJson, self).setUp()
        self.enc_file.write("{}")
        self.enc_json = EncryptedJson(self.path, self.password)

    def test_unexisting_file_getitem_raise_ioerror(self):
        enc_json = EncryptedJson("some_file_that_does_not_exist", self.password)
        with self.assertRaises(IOError):
            some_value = enc_json["some_value"]

    def test_get_unexisting_value_raise_keyerror(self):
        with self.assertRaises(KeyError):
            some_value = self.enc_json["some_value"]

    def test_setitem_and_get_same_item(self):
        content, key = "Hello World", "some_key"
        self.enc_json[key] = content
        self.assertEqual(content, self.enc_json[key])

    def test_setitem_getitem_multiple_items(self):
        keys, values = [], []
        for i in range(10):
            key, value = str(i), "{}_value".format(i)
            keys.append(key)
            values.append(value)
            self.enc_json[key] = value
            self.assertEqual(value, self.enc_json[key])

        for key, value in zip(keys, values):
            self.assertEqual(value, self.enc_json[key])





