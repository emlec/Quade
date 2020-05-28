#!python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import Quade

# Define package info
name = "Quade"
version = Quade.__version__
description = "Fastq files demultiplexer, handling double indexing, molecular indexing and filtering based on index quality"
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=name,
    description=description,
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emlec/Quade",
    author='Adrien Leger & Emilie Lecomte',
    author_email='emilie.lecomte@univ-nantes.fr',
    license='GPLv3',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3'],
    install_requires=[
        'numpy==1.18.1',
        ],
    packages=find_packages()
)
