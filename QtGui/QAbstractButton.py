# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QAbstractButton(QWidget):
    """ QAbstractButton(QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def animateClick(self, int_msecs=100): # real signature unknown; restored from __doc__
        """ QAbstractButton.animateClick(int msecs=100) """
        pass

    def autoExclusive(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.autoExclusive() -> bool """
        return False

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.autoRepeat() -> bool """
        return False

    def autoRepeatDelay(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.autoRepeatDelay() -> int """
        return 0

    def autoRepeatInterval(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.autoRepeatInterval() -> int """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.changeEvent(QEvent) """
        pass

    def checkStateSet(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.checkStateSet() """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.click() """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        """
        QAbstractButton.clicked[bool] [signal]
        QAbstractButton.clicked [signal]
        """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.event(QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.focusInEvent(QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.focusOutEvent(QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.group() -> QButtonGroup """
        return QButtonGroup

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hitButton(self, QPoint): # real signature unknown; restored from __doc__
        """ QAbstractButton.hitButton(QPoint) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.icon() -> QIcon """
        return QIcon

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.iconSize() -> QSize """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.isCheckable() -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.isChecked() -> bool """
        return False

    def isDown(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.isDown() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.keyReleaseEvent(QKeyEvent) """
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nextCheckState(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.nextCheckState() """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def pressed(self, *args, **kwargs): # real signature unknown
        """ QAbstractButton.pressed [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def released(self, *args, **kwargs): # real signature unknown
        """ QAbstractButton.released [signal] """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoExclusive(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractButton.setAutoExclusive(bool) """
        pass

    def setAutoRepeat(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractButton.setAutoRepeat(bool) """
        pass

    def setAutoRepeatDelay(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractButton.setAutoRepeatDelay(int) """
        pass

    def setAutoRepeatInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractButton.setAutoRepeatInterval(int) """
        pass

    def setCheckable(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractButton.setCheckable(bool) """
        pass

    def setChecked(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractButton.setChecked(bool) """
        pass

    def setDown(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractButton.setDown(bool) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QAbstractButton.setIcon(QIcon) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QAbstractButton.setIconSize(QSize) """
        pass

    def setShortcut(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QAbstractButton.setShortcut(QKeySequence) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QAbstractButton.setText(QString) """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.shortcut() -> QKeySequence """
        return QKeySequence

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.text() -> QString """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QAbstractButton.timerEvent(QTimerEvent) """
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ QAbstractButton.toggle() """
        pass

    def toggled(self, *args, **kwargs): # real signature unknown
        """ QAbstractButton.toggled[bool] [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


