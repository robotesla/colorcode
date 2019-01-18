from PySide2.QtCore import QCoreApplication
from settings import preReleasesEnable

def checkUpdatesAvailabe():
    from requests import get
    releasesInformation = get('https://api.github.com/repos/ketsu8/prettycode/releases').json()
    if preReleasesEnable == True:
        latestReleaseInformation = releasesInformation[0]
    else:
        for release in releasesInformation:
            if release['prerelease'] == True: continue
            latestReleaseInformation = release
    currentVersion = QCoreApplication.applicationVersion()
    return False if latestReleaseInformation['tag_name'] == currentVersion else True