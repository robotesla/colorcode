from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from resources import __resourcesDirectory__
from settings import *

_ = returnLanguage(language)

class PreferencesWindow(QDialog):
    def __init__(self, parent=None):
        super(PreferencesWindow, self).__init__(parent)
        self.setupUI()

    def setupTabWidget(self):
        self.tabWidget = QTabWidget()

        interfaceWidget = QWidget()
        interfaceWidget.setLayout(QVBoxLayout())
        interfaceWidget.layout().addStretch(1)

        self.toolbarCheck = QCheckBox(_('Visible Toolbar'))
        self.toolbarCheck.setChecked(toolBarEnable)
        interfaceWidget.layout().addWidget(self.toolbarCheck)

        self.buttomPanelCheck = QCheckBox(_('Visible Buttom Panel'))
        self.buttomPanelCheck.setChecked(buttomPanelEnable)
        interfaceWidget.layout().addWidget(self.buttomPanelCheck)

        self.statusBarCheck = QCheckBox(_('Visible Status Bar'))
        self.statusBarCheck.setChecked(statusBarEnable)
        interfaceWidget.layout().addWidget(self.statusBarCheck)

        self.autoCompleteCheck = QCheckBox(_('Enable Auto Complete (Beta)'))
        self.autoCompleteCheck.setChecked(autoCompleteEnable)
        interfaceWidget.layout().addWidget(self.autoCompleteCheck)

        self.darkThemeCheck = QCheckBox(_('Use Dark Theme'))
        self.darkThemeCheck.setEnabled(False)
        self.darkThemeCheck.setChecked(darkThemeEnable)
        interfaceWidget.layout().addWidget(self.darkThemeCheck)

        self.languageBox = QComboBox()
        
        from settings import languages
        self.languageBox.addItems(languages)
        self.languageBox.setCurrentIndex(self.languageBox.findText(language))
        
        interfaceWidget.layout().addWidget(QLabel(_('Language:')))
        interfaceWidget.layout().addWidget(self.languageBox)

        self.tabWidget.addTab(interfaceWidget, _('Interface'))

        personalWidget = QWidget()
        personalWidget.setLayout(QVBoxLayout())
        personalWidget.layout().addStretch(1)

        self.authorNameEdit = QLineEdit()
        self.authorNameEdit.setPlaceholderText(_('John'))
        self.authorNameEdit.setText(name)
        personalWidget.layout().addWidget(QLabel(_('Name:')))
        personalWidget.layout().addWidget(self.authorNameEdit)

        self.authorEmailEdit = QLineEdit()
        self.authorEmailEdit.setText(email)
        self.authorEmailEdit.setPlaceholderText('johnsmith@mail.com')
        personalWidget.layout().addWidget(QLabel(_('E-mail:')))
        personalWidget.layout().addWidget(self.authorEmailEdit)

        self.countryBox = QComboBox()
        self.countryBox.setCurrentText(country)
        self.countryBox.addItem('Russia')
        self.countryBox.addItem('USA')
        personalWidget.layout().addWidget(QLabel(_('Country:')))
        personalWidget.layout().addWidget(self.countryBox)

        self.tabWidget.addTab(personalWidget, _('Personal'))

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
        settings.setValue('interface/language', self.languageBox.currentText())
        settings.setValue('interface/darkThemeEnable', self.darkThemeCheck.isChecked())
        settings.setValue('interface/toolBarEnable', self.toolbarCheck.isChecked())
        settings.setValue('interface/buttomPanelEnable', self.buttomPanelCheck.isChecked())
        settings.setValue('interface/statusBarEnable', self.statusBarCheck.isChecked())
        settings.setValue('interface/autoCompleteEnable', self.autoCompleteCheck.isChecked())

        settings.setValue('personal/name', self.authorNameEdit.text())
        settings.setValue('personal/email', self.authorEmailEdit.text())
        settings.setValue('personal/country', self.countryBox.currentText())
        settings.sync()
        
        QMessageBox.information(self, 'Saving', 'Preferences successfuly saved.')
        QApplication.quit()

    def setupUI(self):
        self.setupTabWidget()
        self.setupDialogButtonBox()
        self.setupLayout()

        self.setFixedSize(400, 400)
        self.setWindowTitle(_('Preferences'))
