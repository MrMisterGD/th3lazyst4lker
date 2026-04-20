#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="st4lker",
    version="1.1.0",  # bump version
    author="Mr. Mister GD",
    description="lazy OSINT tool for lazy people",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/MrMisterGD/th3lazyst4lker",

    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
        "Topic :: Internet",
    ],

    python_requires=">=3.11",
    install_requires=[
        "sherlock-project>=0.16.0",
        "socialscan>=2.0.1",
        "holehe>=1.61",
        "maigret",
    ],

    entry_points={
        "console_scripts": [
            "st4lker=st4lker.cli:main",
        ],
    },
)