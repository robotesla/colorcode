# only for mac

from os import listdir, walk
from setuptools import setup
from main import __version__, __title__
from os.path import isdir

APP = ['main.py']

DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'resources/branding/test_icon.icns',
    'includes': [dependency.replace('\n', '') for dependency in open('requirements.txt', 'r').readlines()],
    'packages': []
}

setup(
    name=__title__,
    version=__version__,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
