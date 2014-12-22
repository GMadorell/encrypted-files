# encrypted-files

Secure and easy to use encrypted files for Python.

Example:

    from encryptedfiles.encryptedfile import EncryptedFile

    content = "Hello World!"
    enc_file = EncryptedFile(some_path, some_password)
    enc_file.write(content)

    print enc_file.read()  # "Hello World!"
