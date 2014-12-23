import os
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
        self.ensure_exists()
        self.__ensure_data_header_exists()
        with open(self.__path, "r") as fd:
            content = fd.read()
            return decrypt(self.__password, content)

    def is_empty(self):
        return os.path.getsize(self.__path) == 0

    def ensure_exists(self):
        if not os.path.exists(self.__path):
            raise IOError("File doesn't exist.")

    def __ensure_data_header_exists(self):
        if self.is_empty():
            self.write("")




