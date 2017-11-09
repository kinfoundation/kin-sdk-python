#!/usr/bin/env python

from setuptools import setup

exec(open("kin/version.py").read())

setup(
    name='kin-sdk-python',
    version=__version__,
    description='KIN SDK for Python',
    author='Kin Foundation',
    maintainer='David Bolshoy',
    maintainer_email='david.bolshoy@kik.com',
    url='https://github.com/kinfoundation/kin-sdk-python',
    license='MIT',
    packages=["kin"],
    long_description=open("README.md").read(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    install_requires=[
        'six>=1.10.0',
        'asn1crypto>=0.23.0',
        'certifi>=2017.7.27.1',
        'cffi>=1.11.0',
        'chardet>=3.0.4',
        'coincurve>=6.0.0',
        'cytoolz>=0.8.2',
        'ethereum>=2.2.0',
        'ethereum-abi-utils>=0.4.4',
        'ethereum-keys>=0.1.0a7',
        'ethereum-utils>=0.5.1',
        'future>=0.16.0',
        'idna>=2.6',
        'pbkdf2>=1.3',
        'py>=1.4.34',
        'py-ecc>=1.1.3',
        'pycparser>=2.18',
        'pycryptodome>=3.4.7',
        'pyethash>=0.1.27',
        'pylru>=1.0.9',
        'pysha3>=1.0.2',
        'PyYAML>=3.12',
        'repoze.lru>=0.7',
        'requests>=2.18.4',
        'rlp>=0.6.0',
        'scrypt==0.8.0',
        'semantic-version>=2.6.0',
        'toolz>=0.8.2',
        'urllib3>=1.22',
        'web3>=3.16.2',
    ],
)
