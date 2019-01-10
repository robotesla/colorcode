from gettext import translation
from os import listdir
from os.path import dirname, join
from sys import argv

from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

path = join(dirname(argv[0]), 'translations')

languages = []
for language in listdir(path):
    if language.startswith('__'): continue
    languages.append(language)
language = QSettings().value('interface/language', 'en')

def returnLanguage(language):
    return translation('prettycode', path, [language]).gettext

def setLanguage(language):
    settings = QSettings()
    settings.setValue('interface/language', language)
    settings.sync()
    QMessageBox.information(QMainWindow(), 'Setting Language', 'Language successfuly setted. Application need to reload.')
