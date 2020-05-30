"""Information about the package movie-recommendation-system."""
from setuptools import setup, find_packages

PACKAGES = find_packages()
DESCRIPTION = 'An interactive dashboard to find the best movie or TV show ' \
    'recommendation based on the preferences of the user.'
URL = 'https://github.com/flormarcaccio/movie-recommendation-system.git'

OPTS = dict(
    name='movie-recommendation-system',
    description=DESCRIPTION,
    url=URL,
    license='MIT',
    version='1.0',
    packages=PACKAGES
)


if __name__ == '__main__':
    setup(**OPTS)