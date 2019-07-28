from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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

        self.autoCompleteCheck = QCheckBox(_('Enable Auto Complete (Beta)'))
        self.autoCompleteCheck.setChecked(autoCompleteEnable)
        interfaceWidget.layout().addWidget(self.autoCompleteCheck)

        self.languageBox = QComboBox()
        
        from settings import languages
        self.languageBox.addItems(languages)
        self.languageBox.setCurrentIndex(self.languageBox.findText(language))
        
        interfaceWidget.layout().addWidget(QLabel(_('Language:')))
        interfaceWidget.layout().addWidget(self.languageBox)

        self.tabWidget.addTab(interfaceWidget, _('Interface'))

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
        settings.setValue('interface/autoCompleteEnable', self.autoCompleteCheck.isChecked())

        QMessageBox.information(self, _('Saving Settings'), _('Preferences successfully saved. Application needs reload.'))
        QApplication.quit()

    def setupUI(self):
        self.setupTabWidget()
        self.setupDialogButtonBox()
        self.setupLayout()

        self.setFixedSize(400, 400)
        self.setWindowTitle(_('Preferences'))
