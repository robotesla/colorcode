from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from settings import *

_ = returnLanguage(language)

class ProjectCreationWindow(QWizard):
    def __init__(self, parent=None):
        super(ProjectCreationWindow, self).__init__(parent)
        self.setupUI()

    def setupPages(self):
        self.introductionPage = QWizardPage()
        self.introductionPage.setTitle(_('Introduction'))

        layout = QVBoxLayout()
        layout.addWidget(QLabel(_('This wizard will help you create a new . Indicate his name and target platform.')))
        self.introductionPage.setLayout(layout)
        
        self.projectInformationPage = QWizardPage()
        layout = QVBoxLayout()
        self.projectInformationPage.setTitle(_('Project Information'))
        self.projectInformationPage.setSubTitle(_('Let us know something about your project.'))
        
        identifierLabel = QLabel(_('Identifier:'))
        identifierEdit = QLineEdit()
        identifierEdit.setReadOnly(True)
        identifierLabel.setBuddy(identifierEdit)

        nameLabel = QLabel(_('Name:'))
        nameEdit = QLineEdit()
        from settings import name
        nameEdit.textChanged.connect(lambda: identifierEdit.setText('app.{author}.{name}'.format(name=nameEdit.text(), author=name).lower().replace(' ', '-')))
        nameEdit.setText(_('My Project'))
        nameEdit.setPlaceholderText(_('My Project'))
        nameLabel.setBuddy(nameEdit)

        descriptionLabel = QLabel(_('Description:'))
        descriptionEdit = QTextEdit(_('Yet another project.'))
        descriptionLabel.setBuddy(descriptionEdit)

        fpsLabel = QLabel(_('FPS:'))
        fpsEdit = QLineEdit('15')
        fpsLabel.setBuddy(fpsEdit)
        
        watchfaceAppCheck = QCheckBox(_('Allow Watchfacing'))

        layout.addWidget(nameLabel)
        layout.addWidget(nameEdit)
        layout.addWidget(identifierLabel)
        layout.addWidget(identifierEdit)
        layout.addWidget(fpsLabel)
        layout.addWidget(fpsEdit)
        layout.addWidget(descriptionLabel)
        layout.addWidget(descriptionEdit)
        layout.addWidget(watchfaceAppCheck)

        self.projectInformationPage.setLayout(layout)

        self.addPage(self.introductionPage)
        self.addPage(self.projectInformationPage)
    
    def setupUI(self):
        self.setupPages()
        self.setWindowTitle(_('Project Creation'))
        self.setMinimumSize(450, 500)

        from platform import system as currentos
        self.setWizardStyle(QWizard.ModernStyle)
        self.accepted.connect(self.finishCreation)

    def finishCreation(self):
        print('Hello!')