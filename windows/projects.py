from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from resources import __resourcesDirectory__
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

        label = QLabel(_('This wizard will help you create a new project. Indicate his name and target platform.'))
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.introductionPage.setLayout(layout)
        
        # general
        self.projectInformationPage = QWizardPage()
        layout = QVBoxLayout()
        self.projectInformationPage.setTitle(_('Project Information'))
        
        projectNameLabel = QLabel(_('Project Name:'))
        layout.addWidget(projectNameLabel)
        projectNameEdit = QLineEdit()
        layout.addWidget(projectNameEdit)
        projectNameEdit.setPlaceholderText(_('My Project'))
        projectNameLabel.setBuddy(projectNameEdit)

        targetPlatformLabel = QLabel(_('Target Platform:'))
        layout.addWidget(targetPlatformLabel)
        targetPlatformBox = QComboBox()
        layout.addWidget(targetPlatformBox)
        targetPlatformBox.addItem('BetaBoard')
        targetPlatformLabel.setBuddy(targetPlatformBox)
        
        self.projectInformationPage.setLayout(layout)

        # setting pages
        self.addPage(self.introductionPage)
        self.addPage(self.projectInformationPage)
    
    def setupUI(self):
        self.setupPages()
        self.setWindowTitle(_('New Project'))
        self.setMinimumSize(450, 500)
        self.setWizardStyle(QWizard.ModernStyle)
        self.finished.connect(self.finishCreation)

    def finishCreation(self):
        pass