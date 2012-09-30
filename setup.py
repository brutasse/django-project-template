# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(
    name='{{ project_name }}',
    version=__import__('{{ project_name }}').__version__,
    author='Bruno Renie',
    author_email='bruno@renie.fr',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/brutasse/{{ project_name }}',
    license='BSD',
    description='XXX Package description',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=install_requires,
)
