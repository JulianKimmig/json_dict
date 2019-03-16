import time
from distutils.core import setup

import setuptools

setup = dict(name='Json_Dict',
             version="0.2",
             author="Julian Kimmig",
             author_email="julian-kimmig@gmx.net",
             description="Store data in JSON format",
             long_description=open('README.md').read(),
             long_description_content_type="text/markdown",
             url="https://github.com/JulianKimmig/json_dict",
             packages=setuptools.find_packages(),
             classifiers=[
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
             ])
if __name__ == "__main__":
    setuptools.setup(
        **setup
    )
