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

        self.introductionPage.setLayout(QVBoxLayout())
        self.introductionPage.layout().addWidget(QLabel(_('This wizard will help you create a new . Indicate his name and target platform.')))
        
        self.projectInformationPage = QWizardPage()
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


        self.projectInformationPage.setLayout(QVBoxLayout())
        self.projectInformationPage.layout().addWidget(nameLabel)
        self.projectInformationPage.layout().addWidget(nameEdit)
        self.projectInformationPage.layout().addWidget(identifierLabel)
        self.projectInformationPage.layout().addWidget(identifierEdit)
        self.projectInformationPage.layout().addWidget(fpsLabel)
        self.projectInformationPage.layout().addWidget(fpsEdit)
        self.projectInformationPage.layout().addWidget(descriptionLabel)
        self.projectInformationPage.layout().addWidget(descriptionEdit)
        self.projectInformationPage.layout().addWidget(watchfaceAppCheck)

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