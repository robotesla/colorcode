from resources import __resourcesDirectory__
__languagesDirectory__ = __resourcesDirectory__ + 'languages/'

def languageData(language) -> dict:
    from yaml import load
    return load(open(__languagesDirectory__ + language + '.yml', 'r'))

def languagesList() -> dict:
    languages = {}
    from os import listdir
    for language in listdir(__languagesDirectory__):
        if not language.endswith('.yml'): continue
        languages[language.replace('.yml', '')] = language
    return languages
        