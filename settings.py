from gettext import translation
from os import listdir
from os.path import dirname, join
from sys import argv

from PySide2.QtCore import QSettings

path = join(dirname(argv[0]), 'translations')
settings = QSettings()

languages = []
for language in listdir(path):
    if language.startswith('__'): continue
    languages.append(language)

language = settings.value('interface/language', 'en_EN')
darkThemeEnable = True if settings.value('interface/darkThemeEnable', 'true') == 'true' else False
toolBarEnable = True if settings.value('interface/toolBarEnable', 'true') == 'true' else False
buttomPanelEnable = True if settings.value('interface/buttomPanelEnable', 'false') == 'true' else False
statusBarEnable = True if settings.value('interface/statusBarEnable', 'true') == 'true' else False
autoCompleteEnable = True if settings.value('interface/autoCompleteEnable', 'false') == 'true' else False
name = settings.value('personal/name', '')
email = settings.value('personal/email', '')
country = settings.value('personal/country', 'Russia')

def returnLanguage(language):
    return translation('prettycode', path, [language]).gettext
