from distutils.core import setup
import sys

import yeelink 

kw = dict(
    name = 'yeelink',
    version = yeelink.__version__,
    description = 'Python client SDK for Micro Message Public Platform API.',
    long_description = open('README', 'r').read(),
    author = 'Liang Cha',
    author_email = 'ckmx945@gmail.com',
    url = 'https://github.com/kun945/yeelink',
    download_url = 'https://github.com/kun945/yeelink',
    py_modules = ['yeelink'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

setup(**kw)
