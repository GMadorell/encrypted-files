from distutils.core import setup
from setuptools import find_packages


desc = open("README.md").read()

setup(
    name='encryptedfiles',
    version='0.0.3',
    keywords=['secure', 'crypto', 'cryptography', 'encrypt', 'decrypt',
              'encryption', 'decryption'],
    url='https://github.com/Skabed/encrypted-files',
    license=open("LICENSE").read(),
    author='skabed',
    description="Secure and easy to use encrypted files for Python.",
    long_description=desc,
    packages=find_packages(),
    requires="simple_crypt",
    install_requires=["simple_crypt"],

    classifiers=['Intended Audience :: Developers',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Security',
                 'Topic :: Security :: Cryptography',
                 'Topic :: Software Development'],
)
