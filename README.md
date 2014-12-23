# encrypted-files

Secure and easy to use encrypted files for Python.


## How to install ##

    pip install encryptedfiles



Example:

    from encryptedfiles.encryptedfile import EncryptedFile

    content = "Hello World!"
    enc_file = EncryptedFile(some_path, some_password)
    enc_file.write(content)

    print enc_file.read()  # "Hello World!"


Json Example

    from encryptedfiles.encryptedjson import EncryptedJson

    enc_json = EncryptedJson(some_path, some_password)
    api_key = enc_json["API_KEY"]

    enc_json["SOME_OTHER_API_KEY"] = "some_apy_key_here"
