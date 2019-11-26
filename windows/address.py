from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class BridgeSetupDialog(QWizard):
    def __init__(self, parent=None):
        super(BridgeSetupDialog, self).__init__(parent)
        self.setupUI()

    def setupPages(self):
        self.introductionPage = QWizardPage()
        self.introductionPage.setTitle('Introduction')

        self.introductionPage.setLayout(QVBoxLayout())
        self.introductionPage.layout().addWidget(
            QLabel('This wizard will help you setup a Colorboard.'))

        self.projectInformationPage = QWizardPage()
        self.projectInformationPage.setTitle('Device Information')
        self.projectInformationPage.setSubTitle('Let us know something about your device.')

        addressLabel = QLabel('IP Address:')
        self.addressEdit = QLineEdit()
        self.addressEdit.setPlaceholderText('192.168.1.23')
        addressLabel.setBuddy(self.addressEdit)

        self.projectInformationPage.setLayout(QVBoxLayout())
        self.projectInformationPage.layout().addWidget(addressLabel)
        self.projectInformationPage.layout().addWidget(self.addressEdit)

        self.addPage(self.introductionPage)
        self.addPage(self.projectInformationPage)

    def setupUI(self):
        self.setupPages()
        self.setWindowTitle('Device Setup')
        self.setMinimumSize(450, 500)
        self.setWizardStyle(QWizard.ModernStyle)
