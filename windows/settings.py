from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from resources import __resourcesDirectory__

class PreferencesWindow(QDialog):
    def __init__(self, parent=None):
        super(PreferencesWindow, self).__init__(parent)
        self.setupUI()

    def setupTabWidget(self):
        self.tabWidget = QTabWidget()

        interfaceWidget = QWidget()
        interfaceWidget.setLayout(QVBoxLayout())
        interfaceWidget.layout().addStretch(1)

        self.toolbarCheck = QCheckBox('Visible Toolbar')
        interfaceWidget.layout().addWidget(self.toolbarCheck)

        self.buttomPanelCheck = QCheckBox('Visible Buttom Panel')
        interfaceWidget.layout().addWidget(self.buttomPanelCheck)

        self.statusBarCheck = QCheckBox('Visible Status Bar')
        interfaceWidget.layout().addWidget(self.statusBarCheck)

        self.autoCompleteCheck = QCheckBox('Enable Auto Complete (Beta)')
        interfaceWidget.layout().addWidget(self.autoCompleteCheck)

        self.languageBox = QComboBox()
        
        from translations import languages
        self.languageBox.addItems(languages)

        interfaceWidget.layout().addWidget(QLabel('Language:'))
        interfaceWidget.layout().addWidget(self.languageBox)

        self.tabWidget.addTab(interfaceWidget, 'Interface')

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