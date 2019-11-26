from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from windows.address import BridgeSetupDialog
from windows.mainwindow import MainWindow
from bridge import BridgeManager

__version__ = '0.0.1.1-demo'
__title__ = 'Colorcode'


def init():
    QCoreApplication.setApplicationName(__title__)
    QCoreApplication.setOrganizationName('Breitburg Ilya')
    QCoreApplication.setApplicationVersion(__version__)
    app = QApplication([])

    from warnings import filterwarnings
    filterwarnings('ignore')

    from qtmodern.styles import dark
    dark(app)

    setupDialog = BridgeSetupDialog()
    setupDialog.setModal(True)
    setupDialog.show()
    setupDialog.exec_()

    bridge = BridgeManager(baseUrl=setupDialog.addressEdit.text())
    window = MainWindow(bridge)
    window.setMinimumSize(300, 400)
    window.resize(740, 512)
    window.show()

    app.exec_()


if __name__ == '__main__':
    try:
        init()
    except Exception as exception:
        messageBox = QMessageBox()
        messageBox.setText('Initialization error')
        messageBox.setInformativeText('The error that occurred caused the program to stop working.')
        messageBox.setStandardButtons(QMessageBox.Close)
        messageBox.setDefaultButton(QMessageBox.Close)
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setDetailedText(str(exception))
        messageBox.resize(400, 500)
        messageBox.exec()
        QApplication.quit()
