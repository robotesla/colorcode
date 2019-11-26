from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from threading import Thread
from time import sleep

from widgets.codeedit import QCodeEdit
from resources import __resourcesDirectory__


class MainWindow(QMainWindow):
    def __init__(self, bridge):
        super(MainWindow, self).__init__()
        self.bridge = bridge
        self.setupUI()
        self.logsUpdater = Thread(target=self.updateLogs)
        self.logsUpdater.start()

    def setupEditor(self):
        self.editor = QCodeEdit()
        self.editor.cursorPositionChanged.connect(lambda: self.lineStatusLabel.setText('Ln {line}, Col {column}'.format(column='<b>' + str(self.editor.textCursor().columnNumber() + 1) + '</b>', line='<b>' + str(self.editor.textCursor().blockNumber() + 1) + '</b>')))

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

        from os.path import join
        self.toolbar.addAction(QIcon(join(__resourcesDirectory__, 'icons', 'run.png')), 'Build and Run', self.uploadFirmware)

    def uploadFirmware(self):
        self.statusBar().showMessage('Uploading firmware...')
        self.bridge.upload(content=self.editor.toPlainText())
        self.statusBar().showMessage('New firmware successfully uploaded...')
        self.bottomPanel.clear()

    def updateLogs(self):
        while True:
            self.bottomPanel.addItems(self.bridge.getLog())
            print('Updating logs')
            sleep(0.5)

    def setupbottomPanel(self):
        self.statusBar().showMessage('Setting-up bottom panel...')
        self.bottomPanel = QListWidget()
        self.bottomPanel.setStyleSheet('color: white; padding: 10px; selection-background-color: #37373D; background: #252526; border-radius: 0px;')

    def setupMenubar(self):
        self.statusBar().showMessage('Setting-up menubar...')

        styleSheet = 'color: white; background: #3A3935; border-radius: 0px; min-height: 25px; spacing: 18px'
        self.menuBar().setStyleSheet(styleSheet)

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
        fontFormatMenu.addAction('Restore Defaults', lambda: self.editor.setFont(self.editor.getFont()), 'Ctrl+0')

        windowMenu = self.menuBar().addMenu('Window')
        windowMenu.addAction('Minimize', lambda: self.showMinimized(), 'Ctrl+M')
        windowMenu.addAction('Zoom', lambda: self.showMaximized())

        helpMenu = self.menuBar().addMenu('Help')
        helpMenu.addAction('About {productName}'.format(productName=QCoreApplication.applicationName()),
                           lambda: QMessageBox.about(
                               self, 'About {productName}'.format(productName=QCoreApplication.applicationName()),
                               'Pretty development IDE.\nVersion: {productVersion}'.format(productVersion=QCoreApplication.applicationVersion())))
        helpMenu.addAction('About Qt', lambda: QMessageBox.aboutQt(self, 'About Qt'))

    def setupSplitter(self):
        self.statusBar().showMessage('Setting-up splitter...')
        self.splitter = QSplitter()
        self.splitter.setStyleSheet('background: #252526; border-radius: 0px;')
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.bottomPanel)

    def setupStatusbar(self):
        self.statusBar().setStyleSheet('color: white; spacing: 15px; background: #A700C5; border-radius: 0px;')
        self.lineStatusLabel = QLabel('Ln {line}, Col {column}'.format(column='<b>1</b>', line='<b>1</b>'))
        self.statusBar().addPermanentWidget(self.lineStatusLabel)

    def setupUI(self):
        self.setupStatusbar()
        self.setupEditor()
        self.setupToolbar()
        self.setupbottomPanel()
        self.setupMenubar()
        self.setupCompleter()
        self.setupSplitter()
        self.setCentralWidget(self.splitter)
        self.statusBar().showMessage('All set!')
        self.setWindowTitle(QCoreApplication.applicationName())
        self.setUnifiedTitleAndToolBarOnMac(True)