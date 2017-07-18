#!/usr/bin/env python
"""
setup.py for ohms_tools
"""

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

ohms_tools_dev = {
    'develop':
        [
            "pep8-naming>=0.3.3",   # MIT license
            "flake8>=2.5.1",        # MIT license
            "pyflakes>=1.0.0",      # MIT license
            "coverage",
        ]
}

setup(
    name='ohms_tools',
    version='0.1.0',
    description='Ohms Tools is a Python API for dealing with Ohms Law and Power',
    author='Dimitar Dimitrov',
    author_email='targolini@gmail.com',
    url='https://github.com/dimddev/ohms-tools',
    packages=find_packages(),
    test_suite='ohms_tools.tests',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD3 License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
    ext_modules = [Extension('ohms', [cythonize("ohms_tools/api/ohms.pyx")]),
    extras_require=ohms_tools_dev
)
