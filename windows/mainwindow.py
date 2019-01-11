from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.codeedit import QCodeEdit
from windows.settings import PreferencesWindow

from resources import __resourcesDirectory__
from translations import language, returnLanguage

_ = returnLanguage(language)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUI()

    def setupEditor(self):
        self.editor = QCodeEdit()
        self.editor.cursorPositionChanged.connect(lambda: self.lineStatusLabel.setText(_('Ln {line}, Col {column}').format(column='<b>' + str(self.editor.textCursor().columnNumber() + 1) + '</b>', line='<b>' + str(self.editor.textCursor().blockNumber() + 1) + '</b>')))
    
    def setupCompleter(self):
        self.statusBar().showMessage(_('Setting-up completer...'))
        self.completer = QCompleter(self)
        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setWrapAround(False)
        self.completer.setModel(QStringListModel([], self.completer))
        self.editor.setCompleter(self.completer)

    def setupToolbar(self):
        self.statusBar().showMessage(_('Setting-up toolbar...'))
        self.toolbar = QToolBar('Toolbar')
        self.toolbar.setStyleSheet('padding: 8px; background: #333333; border-radius: 0px; spacing: 15px;')
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/run.png'), _('Build and Run'))
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/package.png'), _('Build in package'))
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/settings.png'), _('Project Settings'))
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/open.png'), _('Open Project'))
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/save.png'), _('Save Project'))

    def setupButtomPanel(self):
        self.statusBar().showMessage(_('Setting-up buttom panel...'))
        self.buttomPanel = QListView()
        self.buttomPanel.setStyleSheet('color: white; padding: 10px; selection-background-color: #37373D; background: #252526; border-radius: 0px;')
        model = QStandardItemModel()
        self.buttomPanel.setModel(model)
        self.buttomPanel.setVisible(False)

    def setupMenubar(self):
        self.statusBar().showMessage(_('Setting-up menubar...'))
        
        styleSheet = 'color: white; background: #3A3935; border-radius: 0px; min-height: 25px; spacing: 18px;'
        self.menuBar().setStyleSheet(styleSheet)
        
        fileMenu = self.menuBar().addMenu(_('File'))
        fileMenu.addAction(_('Preferences'), lambda: PreferencesWindow(self).showNormal())
        
        editMenu = self.menuBar().addMenu(_('Edit'))
        editMenu.addAction(_('Undo'), lambda: self.editor.undo(), 'Ctrl+Z')
        editMenu.addAction(_('Redo'), lambda: self.editor.redo(), 'Ctrl+Y')
        editMenu.addSeparator()
        editMenu.addAction(_('Cut'), lambda: self.editor.cut(), 'Ctrl+X')
        editMenu.addAction(_('Copy'), lambda: self.editor.copy(), 'Ctrl+C')
        editMenu.addAction(_('Paste'), lambda: self.editor.paste(), 'Ctrl+V')

        selectionMenu = self.menuBar().addMenu(_('Selection'))
        selectionMenu.addAction(_('Select All'), lambda: self.editor.selectAll(), 'Ctrl+A')

        formatMenu = self.menuBar().addMenu(_('Format'))
        fontFormatMenu = formatMenu.addMenu(_('Font'))
        fontFormatMenu.addAction(_('Zoom In'), lambda: self.editor.zoomIn(), 'Ctrl++')
        fontFormatMenu.addAction(_('Zoom Out'), lambda: self.editor.zoomOut(), 'Ctrl+-')

        viewMenu = self.menuBar().addMenu(_('View'))
        viewMenu.addAction(_('Toggle Toolbar'), lambda: self.toolbar.setVisible(not self.toolbar.isVisible()), 'Ctrl+B')
        viewMenu.addAction(_('Toggle Buttom Panel'), lambda: self.buttomPanel.setVisible(not self.buttomPanel.isVisible()), 'Ctrl+J')
        viewMenu.addAction(_('Toggle Statusbar'), lambda: self.statusBar().setVisible(not self.statusBar().isVisible()), 'Ctrl+M')

        windowMenu = self.menuBar().addMenu(_('Window'))
        windowMenu.addAction(_('Minimize'), lambda: self.showMinimized(), 'Ctrl+M')
        windowMenu.addAction(_('Zoom'), lambda: self.showMaximized())
        

        helpMenu = self.menuBar().addMenu(_('Help'))
        helpMenu.addAction(_('About {productName}').format(productName=QCoreApplication.applicationName()), lambda: QMessageBox.about(self, _('About {productName}').format(productName=QCoreApplication.applicationName()), 'Pretty development IDE.\nVersion: {productVersion}'.format(QCoreApplication.applicationVersion())))
        helpMenu.addAction(_('About Qt'), lambda: QMessageBox.aboutQt(self, _('About Qt')))

    def setupSplitter(self):
        self.statusBar().showMessage(_('Setting-up splitter...'))
        self.splitter = QSplitter()
        self.splitter.setStyleSheet('background: #252526; border-radius: 0px;')
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.buttomPanel)

    def setupStatusbar(self):
        self.statusBar().setStyleSheet('color: white; spacing: 15px; background: #A700C5; border-radius: 0px;')
        self.lineStatusLabel = QLabel(_('Ln {line}, Col {column}').format(column='<b>1</b>', line='<b>1</b>'))
        self.statusBar().addPermanentWidget(self.lineStatusLabel)

    def setupUI(self):
        self.setupStatusbar()
        self.setupEditor()
        self.setupToolbar()
        self.setupButtomPanel()
        self.setupMenubar()
        self.setupCompleter()
        self.setupSplitter()
        self.setCentralWidget(self.splitter)
        self.statusBar().showMessage(_('All set!'))
        self.setWindowTitle(QCoreApplication.applicationName())
        self.setUnifiedTitleAndToolBarOnMac(True)