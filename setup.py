
from setuptools import setup

setup(
    name = 'LsaDecryptXp',
    version = '1.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security :: Cryptography',
    ],

    author = 'Francesco "dfirfpi" Picasso',
    author_email = 'francesco.picasso@gmail.com',
    description = 'NT 5.[12] LsaUnprotectMemory',
    long_description=open('README.rst').read(),
    license = "GPLv2+",
    url = 'https://github.com/dfirfpi/lsadecryptxp',
    keywords = '',

    py_modules = ['lsadecryptxp'],
    test_suite='lsatest',
    zip_safe=True,
    use_2to3=True,
)