from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class PreferencesWindow(QDialog):
    def __init__(self, parent=None):
        super(PreferencesWindow, self).__init__(parent)
        self.setupUI()

    def setupTabWidget(self):
        self.tabWidget = QTabWidget()

        generalWidget = QWidget()
        generalWidget.setLayout(QVBoxLayout())
        generalWidget.layout().addStretch(1)
        generalWidget.layout().setSpacing(20)

        self.toolbarCheck = QCheckBox('Visible Toolbar')
        self.buttomPanelCheck = QCheckBox('Visible Buttom Panel')
        self.statusBarCheck = QCheckBox('Visible Status Bar')
        self.autoCompleteCheck = QCheckBox('Enable Auto Complete (Beta)')
        generalWidget.layout().addWidget(self.toolbarCheck)
        generalWidget.layout().addWidget(self.buttomPanelCheck)
        generalWidget.layout().addWidget(self.statusBarCheck)
        generalWidget.layout().addWidget(self.autoCompleteCheck)

        self.tabWidget.addTab(generalWidget, 'General')

        personalWidget = QWidget()
        personalWidget.setLayout(QVBoxLayout())
        personalWidget.layout().addStretch(1)

        self.authorNameEdit = QLineEdit()
        self.authorNameEdit.setPlaceholderText('John')
        personalWidget.layout().addWidget(QLabel('Name:'))
        personalWidget.layout().addWidget(self.authorNameEdit)

        self.authorEmailEdit = QLineEdit()
        self.authorEmailEdit.setPlaceholderText('johnsmith@mail.com')
        personalWidget.layout().addWidget(QLabel('E-mail:'))
        personalWidget.layout().addWidget(self.authorEmailEdit)

        self.countryBox = QComboBox()
        self.countryBox.addItem('Russia')
        self.countryBox.addItem('USA')
        personalWidget.layout().addWidget(QLabel('Country:'))
        personalWidget.layout().addWidget(self.countryBox)

        self.tabWidget.addTab(personalWidget, 'Personal')

    def setupDialogButtonBox(self):
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
        self.buttonBox.accepted.connect(self.saveSettings)
        self.buttonBox.rejected.connect(self.reject)

    def setupLayout(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.tabWidget)
        self.mainLayout.addWidget(self.buttonBox)
        self.setLayout(self.mainLayout)

    def saveSettings(self):
        QMessageBox.warning(self, 'Saving', 'Saving in development.')
        self.close()

    def setupUI(self):
        self.setupTabWidget()
        self.setupDialogButtonBox()
        self.setupLayout()

        self.setFixedSize(400, 400)
        self.setWindowTitle('Preferences')