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
        
        # introduction
        self.introductionPage = QWizardPage()
        self.introductionPage.setTitle(_('Introduction'))
        self.introductionPage.setSubTitle(_('This wizard will help you create a new project. Indicate his name and target platform.'))

        layout = QVBoxLayout()
        self.introductionPage.setLayout(layout)
        
        # general
        self.projectInformationPage = QWizardPage()
        layout = QVBoxLayout()
        self.projectInformationPage.setTitle(_('Project Information'))
        self.projectInformationPage.setSubTitle(_('Let us know something about your project.'))
        
        projectIdentifierLabel = QLabel(_('Project Identifier:'))
        projectIdentifierEdit = QLineEdit()
        projectIdentifierEdit.setReadOnly(True)
        projectIdentifierEdit.setText('app.unknown.untitled')
        projectIdentifierLabel.setBuddy(projectIdentifierEdit)

        projectNameLabel = QLabel(_('Project Name:'))
        projectNameEdit = QLineEdit()
        from settings import name
        projectNameEdit.textChanged.connect(lambda: projectIdentifierEdit.setText('app.{author}.{name}'.format(name=projectNameEdit.text(), author=name).lower().replace(' ', '-')))
        projectNameEdit.setPlaceholderText(_('My Project'))
        projectNameEdit.setText(_('My Project'))
        projectNameLabel.setBuddy(projectNameEdit)

        targetPlatformLabel = QLabel(_('Target Platform:'))
        targetPlatformBox = QComboBox()
        targetPlatformBox.addItem('BetaBoard')
        targetPlatformLabel.setBuddy(targetPlatformBox)
        
        layout.addWidget(projectNameLabel)
        layout.addWidget(projectNameEdit)
        layout.addWidget(projectIdentifierLabel)
        layout.addWidget(projectIdentifierEdit)
        layout.addWidget(targetPlatformLabel)
        layout.addWidget(targetPlatformBox)

        self.projectInformationPage.setLayout(layout)

        # setting pages
        self.addPage(self.introductionPage)
        self.addPage(self.projectInformationPage)
    
    def setupUI(self):
        self.setupPages()
        self.setWindowTitle(_('New Project'))
        self.setMinimumSize(450, 500)

        from platform import system as currentos
        self.setWizardStyle(QWizard.ModernStyle)
        self.finished.connect(self.finishCreation)

    def finishCreation(self):
        print('Hello!')