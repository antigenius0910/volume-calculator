# setup.py
from setuptools import setup, find_packages

setup(
    name="volume_calculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="A simple library to calculate volumes of various geometric shapes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/antigenius0910/volume_calculator",
    author="yen",
    author_email="email@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
