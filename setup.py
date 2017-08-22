from setuptools import find_packages, setup


with open('README.md') as file:
    long_description = file.read()

setup(
    name='tesco',
    version='0.1.0',
    description='Python module for interacting with the Tesco API.',
    long_description=long_description,
    url='https://github.com/thomasleese/pytesco',
    author='Thomas Leese',
    author_email='thomas@leese.io',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)
