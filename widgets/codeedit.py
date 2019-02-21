
from platform import system as platform

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from jedi import Script


class QCodeEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super(QCodeEdit, self).__init__(parent)

        self._completer = None
        self.lastItems = []
        
        font = QFont()
        font.setFamily('Menlo' if platform() == 'Darwin' else ('Consoleas' if platform() == 'Windows' else 'Courier'))
        font.setFixedPitch(True)
        font.setPointSize(13 if platform() == 'Darwin' else 10)

        self.setFont(font)

        from settings import autoCompleteEnable
        self.setStyleSheet('color: white; padding: 10px; background: #1E1E1E; border-radius: 0px')
        
        self.setPlaceholderText('Maybe, you should write a couple of lines of code here...')
        self.setTabStopDistance(35)
        self.setPlainText('from matrix import *\n\ndef setup():\n\tpass\n\ndef frame():\n\tpass')

        from widgets.highlight import PythonHighlighter
        self.highlighter = PythonHighlighter(self.document())

        self.completionsTimer = QTimer(self, interval=750, timeout=self.makeCompletions)

        if autoCompleteEnable == True: self.completionsTimer.start()

    def setCompleter(self, c):
        if self._completer is not None:
            self._completer.activated.disconnect()

        self._completer = c
        c.setWidget(self)
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(Qt.CaseInsensitive)
        c.activated.connect(self.insertCompletion)
        self._completer.popup().setStyleSheet('color: white; background: #2A2A2A; border-radius: 10px')

    def makeCompletions(self):
        currentLineNumber = self.textCursor().blockNumber()
        if self.toPlainText().replace('\t', '').replace(' ', '').replace('\n', '') == '': return 
        
        try: items = [i.name for i in Script(source=self.toPlainText(), line=currentLineNumber + 1, column=self.textCursor().columnNumber()).completions()]
        except ValueError: return 
        
        if self.lastItems == items: return
        self._completer.setModel(QStringListModel(items, self._completer))
        self.lastItems = items

    def completer(self):
        return self._completer

    def insertCompletion(self, completion):
        if self._completer.widget() is not self:
            return

        tc = self.textCursor()
        extra = len(completion) - len(self._completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)

        return tc.selectedText()

    def focusInEvent(self, e):
        if self._completer is not None:
            self._completer.setWidget(self)

        super(QCodeEdit, self).focusInEvent(e)

    def keyPressEvent(self, e):
        if self._completer is not None and self._completer.popup().isVisible():
            if e.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                e.ignore()
                return
        
        super(QCodeEdit, self).keyPressEvent(e)
        cr = self.cursorRect()
        cr.setWidth(self._completer.popup().sizeHintForColumn(0) + self._completer.popup().verticalScrollBar().sizeHint().width())
        self._completer.complete(cr)
