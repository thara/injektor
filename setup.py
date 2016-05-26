#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import injektor


setup(
    name='injektor',
    version=injektor.__version__,
    description='a Pythonic dependency injection framework',
    long_description=injektor.__doc__,
    author=injektor.__author__,
    url='https://github.com/tomochikahara/injektor',
    py_modules=['injektor'],
    license='MIT',
    platforms='any',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 ],
    keywords=['Dependency Injection',
              'DI',
              'Dependency Injection framework',
              'Inversion of Control',
              'IoC',
              'Inversion of Control container',
              ],
    )
