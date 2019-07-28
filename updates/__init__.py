from PySide2.QtCore import QCoreApplication
from settings import preReleasesEnable


def checkUpdatesAvailable():
    from requests import get
    releasesInformation = get('https://api.github.com/repos/ketsu8/colorcode/releases').json()
    
    currentVersion = QCoreApplication.applicationVersion()
    latestReleaseInformation = {'tag_name' : currentVersion}

    if preReleasesEnable == True:
        latestReleaseInformation = releasesInformation[0]
    else:
        for release in releasesInformation:
            if release['prerelease'] == True: continue
            latestReleaseInformation = release

    return False if latestReleaseInformation['tag_name'] == currentVersion else True
