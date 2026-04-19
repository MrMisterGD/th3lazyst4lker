#!/usr/bin/env python3
"""setup for st4lker - install with: pip install -e ."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="st4lker",
    version="1.0.0",
    author="Mr. Mister GD",
    description="lazy OSINT tool for lazy people",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/th3lazyst4lker",
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
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "st4lker=st4lker.cli:main",
        ],
    },
)
