import json
from encryptedfiles.encryptedfile import EncryptedFile


class EncryptedJson(object):
    def __init__(self, path, password):
        self.__dirty = True
        self.__content = None
        self.enc_file = EncryptedFile(path, password)

    def __getitem__(self, item):
        content = self.get_content_dictionary()
        return content.__getitem__(item)

    def __setitem__(self, key, value):
        content = self.get_content_dictionary()
        content.__setitem__(key, value)
        self.enc_file.write(json.dumps(content))
        self.__dirty = True

    def get_content_dictionary(self):
        if self.__dirty:
            self.__dirty = False
            self.enc_file.ensure_exists()
            self.__ensure_json_if_empty()
            self.__content = json.loads(self.enc_file.read())
        return self.__content

    def __ensure_json_if_empty(self):
        if self.enc_file.is_empty():
            self.enc_file.write("{}")



