from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.codeedit import QCodeEdit
from windows.settings import PreferencesWindow

__resourcesDirectory__ = 'resources/'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUI()

    def setupEditor(self):
        self.editor = QCodeEdit()
        self.editor.cursorPositionChanged.connect(lambda: self.lineStatusLabel.setText('Ln <b>' + str(self.editor.textCursor().blockNumber() + 1) + '</b>, Col <b>' + str(self.editor.textCursor().columnNumber() + 1) + '</b>'))
    
    def setupCompleter(self):
        self.statusBar().showMessage('Setting-up completer...')
        self.completer = QCompleter(self)
        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setWrapAround(False)
        self.completer.setModel(QStringListModel([], self.completer))
        self.editor.setCompleter(self.completer)

    def setupToolbar(self):
        self.statusBar().showMessage('Setting-up toolbar...')
        self.toolbar = QToolBar('Toolbar')
        self.toolbar.setStyleSheet('padding: 8px; background: #333333; border-radius: 0px; spacing: 15px;')
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/run.png'), 'Build and Run')
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/package.png'), 'Build in package')
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/settings.png'), 'Project Settings')
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/open.png'), 'Open Project')
        self.toolbar.addAction(QIcon(__resourcesDirectory__ + 'icons/save.png'), 'Save Project')

    def setupButtomPanel(self):
        self.statusBar().showMessage('Setting-up buttom panel...')
        self.buttomPanel = QListView()
        self.buttomPanel.setStyleSheet('color: white; padding: 10px; selection-background-color: #37373D; background: #252526; border-radius: 0px;')
        model = QStandardItemModel()
        self.buttomPanel.setModel(model)
        self.buttomPanel.setVisible(False)

    def setupMenubar(self):
        self.statusBar().showMessage('Setting-up menubar...')
        self.menuBar().setStyleSheet('color: white; background: #3A3935; border-radius: 0px; min-height: 25px; spacing: 18px; selection-background-color: #37373D;')
        
        fileMenu = self.menuBar().addMenu('File')
        fileMenu.addAction('Preferences', lambda: PreferencesWindow(self).showNormal())
        
        editMenu = self.menuBar().addMenu('Edit')
        editMenu.addAction('Undo', lambda: self.editor.undo(), 'Ctrl+Z')
        editMenu.addAction('Redo', lambda: self.editor.redo(), 'Ctrl+Y')
        editMenu.addSeparator()
        editMenu.addAction('Cut', lambda: self.editor.cut(), 'Ctrl+X')
        editMenu.addAction('Copy', lambda: self.editor.copy(), 'Ctrl+C')
        editMenu.addAction('Paste', lambda: self.editor.paste(), 'Ctrl+V')

        selectionMenu = self.menuBar().addMenu('Selection')
        selectionMenu.addAction('Select All', lambda: self.editor.selectAll(), 'Ctrl+A')

        formatMenu = self.menuBar().addMenu('Format')
        fontFormatMenu = formatMenu.addMenu('Font')
        fontFormatMenu.addAction('Zoom In', lambda: self.editor.zoomIn(), 'Ctrl++')
        fontFormatMenu.addAction('Zoom Out', lambda: self.editor.zoomOut(), 'Ctrl+-')

        viewMenu = self.menuBar().addMenu('View')
        viewMenu.addAction('Toggle Toolbar', lambda: self.toolbar.setVisible(not self.toolbar.isVisible()), 'Ctrl+B')
        viewMenu.addAction('Toggle Buttom Panel', lambda: self.buttomPanel.setVisible(not self.buttomPanel.isVisible()), 'Ctrl+J')
        viewMenu.addAction('Toggle Statusbar', lambda: self.statusBar().setVisible(not self.statusBar().isVisible()), 'Ctrl+M')

        windowMenu = self.menuBar().addMenu('Window')
        windowMenu.addAction('Minimize', lambda: self.showMinimized(), 'Ctrl+M')
        windowMenu.addAction('Zoom', lambda: self.showMaximized())
        

        helpMenu = self.menuBar().addMenu('Help')
        helpMenu.addAction('About ' + QCoreApplication.applicationName(), lambda: QMessageBox.about(self, 'About ' + QCoreApplication.applicationName(), 'Pretty development IDE.\nVersion: ' + QCoreApplication.applicationVersion()))
        helpMenu.addAction('About Qt', lambda: QMessageBox.aboutQt(self, 'About Qt'))

    def setupSplitter(self):
        self.statusBar().showMessage('Setting-up splitter...')
        self.splitter = QSplitter()
        self.splitter.setStyleSheet('background: #252526; border-radius: 0px;')
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.buttomPanel)

    def setupStatusbar(self):
        self.statusBar().setStyleSheet('color: white; spacing: 15px; background: #A700C5; border-radius: 0px;')
        self.lineStatusLabel = QLabel('Ln <b>1</b>, Col <b>1</b>')
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
        self.statusBar().showMessage('All set!')
        self.setWindowTitle(QCoreApplication.applicationName())
        self.setUnifiedTitleAndToolBarOnMac(True)

if __name__ == '__main__':
    QCoreApplication.setApplicationName('Prettycode')
    QCoreApplication.setOrganizationDomain('ketsu8')
    QCoreApplication.setOrganizationName('Ketsu8')
    QCoreApplication.setApplicationVersion('dev0')

    app = QApplication([])
    window = MainWindow()
    window.setMinimumSize(640, 512)
    window.show()
    app.exec_()
