#!/usr/bin/env python
import sys
version = sys.argv[1]
del sys.argv[1]
from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name='UQpy',
    version=version,
    url='https://github.com/SURGroup/UQpy',
    description="UQpy is a general purpose toolbox for Uncertainty Quantification",
    long_description=long_description,
    author="Michael D. Shields, Dimitris G. Giovanis, Audrey Olivier, Aakash Bangalore-Satish, Mohit Chauhan, "
           "Lohit Vandanapu, Ketson R.M. dos Santos",
    license='MIT',
    platforms=["OSX", "Windows", "Linux"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.pdf"]},
    python_requires='>3.9.0',
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest == 8.4.0',
            'pytest-cov == 6.1.1',
            'pylint == 3.3.7',
            'pytest-azurepipelines == 1.0.5',
            'pytest-cov == 6.1.1',
            'wheel == 0.45.1',
            'twine == 6.1.0',
            'sphinx_autodoc_typehints == 1.23.0',
            'sphinx_rtd_theme == 1.2.0',
            'sphinx_gallery == 0.13.0',
            'sphinxcontrib_bibtex == 2.5.0',
            'Sphinx==6.1.3',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
)
