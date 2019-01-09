from gettext import translation
from sys import argv
from os.path import join, dirname
from os import listdir

path = join(dirname(argv[0]), 'translations')

languages = listdir(path)
languages.remove('__pycache__')
languages.remove('__init__.py')

def returnLanguage(language):
    return translation('prettycode', path, [language]).gettext