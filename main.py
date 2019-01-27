from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from windows.mainwindow import MainWindow

if __name__ == '__main__':
    QCoreApplication.setApplicationName('Colorcode')
    QCoreApplication.setOrganizationName('Ketsu8')
    QCoreApplication.setApplicationVersion('0.0.1.1')
    app = QApplication([])

    from warnings import filterwarnings
    filterwarnings('ignore')

    from settings import returnLanguage, language
    _ = returnLanguage(language)

    from qtmodern.styles import dark
    dark(app)

    from resources import __resourcesDirectory__
    splashPicture = QPixmap(__resourcesDirectory__ + '/splash.png')
    splashScreen = QSplashScreen(splashPicture, Qt.WindowStaysOnTopHint)
    splashScreen.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splashScreen.setEnabled(False)

    progressBar = QProgressBar(splashScreen)
    progressBar.setMaximum(10)
    progressBar.setTextVisible(False)
    progressBar.setGeometry(160, 250, 200, 20)
    splashScreen.showMessage(_('Version: {version}').format(version='<b>' + QCoreApplication.applicationVersion() + '</b>'), Qt.AlignBottom | Qt.AlignRight, Qt.white)
    splashScreen.show()

    from time import time
    for i in range(1, 11):
        progressBar.setValue(i)
        t = time()
        while time() < t + 0.2:
            app.processEvents()
    
    from updates import checkUpdatesAvailable
    if checkUpdatesAvailable() == True: print('Update available.')

    window = MainWindow()
    window.setMinimumSize(300, 400)
    window.resize(740, 512)
    window.show()
    splashScreen.finish(window)
    app.exec_()
