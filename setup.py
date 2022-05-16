# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-test-pep8',
    version='0.1',
    description='PEP8 Tests to Django projects running Python 3',
    long_description='PEP8 Tests to Django projects running Python 3',
    keywords='django test pep8 pycodestyle python3',
    author='Davi Oliveira',
    url='https://github.com/paulj3000/django-test-pep8',
    download_url='https://github.com/paulj3000/django-test-pep8/downloads',
    license='BSD',
    packages=find_packages(),
    install_requires=['pycodestyle', ],
)
