import re

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as fp:
  long_description = fp.read()

with open(path.join(here, 'hues', '__init__.py'), encoding='utf-8') as fp:
  rex = r'^__version__ = \((\d+?), (\d+?), (\d+?)\)$'
  vtp = re.search(rex, fp.read(), re.M).groups()
  __version__ = '.'.join(vtp)

install_requires = []
setup_requires = ['pytest-runner',]
test_requirements = ['pytest', 'coverage',]


setup(
  name='hues',
  version=__version__,
  description='Colored terminal text made easy for Python and happiness.',
  long_description=long_description,
  url='https://github.com/prashnts/hues',
  download_url='https://github.com/prashnts/hues/tarball/' + __version__,
  license='MIT',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords='color colour terminal text ansi hues unicorns',
  packages=['hues'],
  author='Prashant Sinha',
  install_requires=install_requires,
  setup_requires=setup_requires,
  tests_require=test_requirements,
  author_email='prashant@noop.pw'
)
