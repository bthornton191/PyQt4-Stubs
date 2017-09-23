# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QLineEdit(QWidget):
    """
    QLineEdit(QWidget parent=None)
    QLineEdit(QString, QWidget parent=None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ QLineEdit.alignment() -> Qt.Alignment """
        pass

    def backspace(self): # real signature unknown; restored from __doc__
        """ QLineEdit.backspace() """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QLineEdit.clear() """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ QLineEdit.completer() -> QCompleter """
        return QCompleter

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.contextMenuEvent(QContextMenuEvent) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ QLineEdit.copy() """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ QLineEdit.createStandardContextMenu() -> QMenu """
        return QMenu

    def cursorBackward(self, bool, int_steps=1): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorBackward(bool, int steps=1) """
        pass

    def cursorForward(self, bool, int_steps=1): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorForward(bool, int steps=1) """
        pass

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorMoveStyle() -> Qt.CursorMoveStyle """
        pass

    def cursorPosition(self): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorPosition() -> int """
        return 0

    def cursorPositionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorPositionAt(QPoint) -> int """
        return 0

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        """ QLineEdit.cursorPositionChanged[int, int] [signal] """
        pass

    def cursorRect(self): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorRect() -> QRect """
        pass

    def cursorWordBackward(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorWordBackward(bool) """
        pass

    def cursorWordForward(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.cursorWordForward(bool) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ QLineEdit.cut() """
        pass

    def del_(self): # real signature unknown; restored from __doc__
        """ QLineEdit.del_() """
        pass

    def deselect(self): # real signature unknown; restored from __doc__
        """ QLineEdit.deselect() """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def displayText(self): # real signature unknown; restored from __doc__
        """ QLineEdit.displayText() -> QString """
        pass

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ QLineEdit.dragEnabled() -> bool """
        return False

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.dragMoveEvent(QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.dropEvent(QDropEvent) """
        pass

    def echoMode(self): # real signature unknown; restored from __doc__
        """ QLineEdit.echoMode() -> QLineEdit.EchoMode """
        pass

    def editingFinished(self, *args, **kwargs): # real signature unknown
        """ QLineEdit.editingFinished [signal] """
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def end(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.end(bool) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.event(QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.focusInEvent(QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.focusOutEvent(QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def getTextMargins(self): # real signature unknown; restored from __doc__
        """ QLineEdit.getTextMargins() -> (int, int, int, int) """
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ QLineEdit.hasAcceptableInput() -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ QLineEdit.hasFrame() -> bool """
        return False

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ QLineEdit.hasSelectedText() -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def home(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.home(bool) """
        pass

    def initStyleOption(self, QStyleOptionFrame): # real signature unknown; restored from __doc__
        """ QLineEdit.initStyleOption(QStyleOptionFrame) """
        pass

    def inputMask(self): # real signature unknown; restored from __doc__
        """ QLineEdit.inputMask() -> QString """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QLineEdit.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def insert(self, QString): # real signature unknown; restored from __doc__
        """ QLineEdit.insert(QString) """
        pass

    def isModified(self): # real signature unknown; restored from __doc__
        """ QLineEdit.isModified() -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QLineEdit.isReadOnly() -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ QLineEdit.isRedoAvailable() -> bool """
        return False

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ QLineEdit.isUndoAvailable() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maxLength(self): # real signature unknown; restored from __doc__
        """ QLineEdit.maxLength() -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QLineEdit.minimumSizeHint() -> QSize """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QLineEdit.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ QLineEdit.paste() """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ QLineEdit.placeholderText() -> QString """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QLineEdit.redo() """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def returnPressed(self, *args, **kwargs): # real signature unknown
        """ QLineEdit.returnPressed [signal] """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ QLineEdit.selectAll() """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ QLineEdit.selectedText() -> QString """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QLineEdit.selectionChanged [signal] """
        pass

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ QLineEdit.selectionStart() -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QLineEdit.setAlignment(Qt.Alignment) """
        pass

    def setCompleter(self, QCompleter): # real signature unknown; restored from __doc__
        """ QLineEdit.setCompleter(QCompleter) """
        pass

    def setCursorMoveStyle(self, Qt_CursorMoveStyle): # real signature unknown; restored from __doc__
        """ QLineEdit.setCursorMoveStyle(Qt.CursorMoveStyle) """
        pass

    def setCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QLineEdit.setCursorPosition(int) """
        pass

    def setDragEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.setDragEnabled(bool) """
        pass

    def setEchoMode(self, QLineEdit_EchoMode): # real signature unknown; restored from __doc__
        """ QLineEdit.setEchoMode(QLineEdit.EchoMode) """
        pass

    def setFrame(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.setFrame(bool) """
        pass

    def setInputMask(self, QString): # real signature unknown; restored from __doc__
        """ QLineEdit.setInputMask(QString) """
        pass

    def setMaxLength(self, p_int): # real signature unknown; restored from __doc__
        """ QLineEdit.setMaxLength(int) """
        pass

    def setModified(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.setModified(bool) """
        pass

    def setPlaceholderText(self, QString): # real signature unknown; restored from __doc__
        """ QLineEdit.setPlaceholderText(QString) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QLineEdit.setReadOnly(bool) """
        pass

    def setSelection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QLineEdit.setSelection(int, int) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QLineEdit.setText(QString) """
        pass

    def setTextMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLineEdit.setTextMargins(int, int, int, int)
        QLineEdit.setTextMargins(QMargins)
        """
        pass

    def setValidator(self, QValidator): # real signature unknown; restored from __doc__
        """ QLineEdit.setValidator(QValidator) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QLineEdit.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QLineEdit.text() -> QString """
        pass

    def textChanged(self, *args, **kwargs): # real signature unknown
        """ QLineEdit.textChanged[QString] [signal] """
        pass

    def textEdited(self, *args, **kwargs): # real signature unknown
        """ QLineEdit.textEdited[QString] [signal] """
        pass

    def textMargins(self): # real signature unknown; restored from __doc__
        """ QLineEdit.textMargins() -> QMargins """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QLineEdit.undo() """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ QLineEdit.validator() -> QValidator """
        return QValidator

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoEcho = 1
    Normal = 0
    Password = 2
    PasswordEchoOnEdit = 3


