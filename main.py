from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from settings import language, returnLanguage
from windows.mainwindow import MainWindow

_ = returnLanguage(language)
__version__ = '0.0.1.1'
__title__ = 'Colorcode'

def init():
    QCoreApplication.setApplicationName(__title__)
    QCoreApplication.setOrganizationName('Ketsu8')
    QCoreApplication.setApplicationVersion(__version__)
    app = QApplication([])

    if qVersion() != '5.9.4': raise Exception(_('Qt version is too high and incompatible.'))

    from warnings import filterwarnings
    filterwarnings('ignore')

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

if __name__ == '__main__':
    try:
        init()
    except Exception as exception:
        messageBox = QMessageBox()
        messageBox.setText(_('Initialization error'))
        messageBox.setInformativeText(_('The error that occurred caused the program to stop working.'))
        messageBox.setStandardButtons(QMessageBox.Close)
        messageBox.setDefaultButton(QMessageBox.Close)
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setDetailedText(str(exception))
        messageBox.exec()
        QApplication.quit()
