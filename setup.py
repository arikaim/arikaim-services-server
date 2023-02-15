from distutils.core import setup
from setuptools import find_packages
import os

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(

scripts = [
    'arikaim-server',
],
# Project name: 
name='arikaim service server',

# Packages to include in the distribution: 
packages = [
    'arikaim.core',
    'arikaim.core.access',
    'arikaim.core.access.middleware',
    'arikaim.core.access.providers',
    'arikaim.core.console',
    'arikaim.core.console.templates',
    'arikaim.core.db',
    'arikaim.core.queue',
    'arikaim.core.db.models'
],
   
# Project version number:
version='0.5.1',

# List a license for the project, eg. MIT License
license='MIT License',

# Short description of your library: 
description='Arikaim python service server',

# Long description of your library: 
long_description=long_description,
long_description_content_type='text/markdown',

# Your name: 
author='Intersoft Ltd',

# Your email address:
author_email='info@arikaim.com',

# Link to your github repository or website: 
url='',

# Download Link from where the project can be downloaded from:
download_url='',

# List of keywords: 
keywords=['arikaim'],

# List project dependencies: 
install_requires=[   
    'uvicorn',
    'starlette',
    'pymysql',
    'peewee',
    'click',
    'rq',
    'rq-scheduler',
    'rich',
    'requests',
    'pydantic',
    'python-multipart',
    'pymitter'   
],

# https://pypi.org/classifiers/ 
classifiers=[]
)