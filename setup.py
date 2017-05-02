from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()


setup(
    name='mandrill-really-maintained',
    version=version,
    author='Mandrill Devs',
    author_email='community@mandrill.com',
    description=(
        'A really maintained CLI client and Python API library for the '
        'Mandrill email as a service platform.'
    ),
    long_description=long_description,
    license='Apache-2.0',
    keywords='mandrill email api',
    url='https://bitbucket.org/hadrien/mandrill-really-maintained',
    scripts=['scripts/mandrill', 'scripts/sendmail.mandrill'],
    py_modules=['mandrill'],
    install_requires=[
        'docopt >= 0.4.0',
        'requests >= 0.13.2',
    ],
    extras_require={
        'releasing': [
            'bumpversion',
            'twine',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Communications :: Email'
    ]
)
