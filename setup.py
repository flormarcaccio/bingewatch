"""Information about the package bingewatch."""
from setuptools import setup, find_packages

PACKAGES = find_packages()
DESCRIPTION = 'An interactive dashboard to find the best movie or TV show ' \
    'recommendation based on the preferences of the user.'
URL = 'https://github.com/flormarcaccio/bingewatch.git'

OPTS = dict(
    name='bingewatch',
    description=DESCRIPTION,
    url=URL,
    license='MIT',
    version='1.0',
    packages=PACKAGES
)


if __name__ == '__main__':
    setup(**OPTS)