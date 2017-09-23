# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QWorkspace(QWidget):
    """ QWorkspace(QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activateNextWindow(self): # real signature unknown; restored from __doc__
        """ QWorkspace.activateNextWindow() """
        pass

    def activatePreviousWindow(self): # real signature unknown; restored from __doc__
        """ QWorkspace.activatePreviousWindow() """
        pass

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ QWorkspace.activeWindow() -> QWidget """
        return QWidget

    def addWindow(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QWorkspace.addWindow(QWidget, Qt.WindowFlags flags=0) -> QWidget """
        return QWidget

    def arrangeIcons(self): # real signature unknown; restored from __doc__
        """ QWorkspace.arrangeIcons() """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ QWorkspace.background() -> QBrush """
        return QBrush

    def cascade(self): # real signature unknown; restored from __doc__
        """ QWorkspace.cascade() """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.changeEvent(QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.childEvent(QChildEvent) """
        pass

    def closeActiveWindow(self): # real signature unknown; restored from __doc__
        """ QWorkspace.closeActiveWindow() """
        pass

    def closeAllWindows(self): # real signature unknown; restored from __doc__
        """ QWorkspace.closeAllWindows() """
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
        """ QWorkspace.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.eventFilter(QObject, QEvent) -> bool """
        return False

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.hideEvent(QHideEvent) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.resizeEvent(QResizeEvent) """
        pass

    def scrollBarsEnabled(self): # real signature unknown; restored from __doc__
        """ QWorkspace.scrollBarsEnabled() -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveWindow(self, QWidget): # real signature unknown; restored from __doc__
        """ QWorkspace.setActiveWindow(QWidget) """
        pass

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QWorkspace.setBackground(QBrush) """
        pass

    def setScrollBarsEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QWorkspace.setScrollBarsEnabled(bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QWorkspace.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tile(self): # real signature unknown; restored from __doc__
        """ QWorkspace.tile() """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QWorkspace.wheelEvent(QWheelEvent) """
        pass

    def windowActivated(self, *args, **kwargs): # real signature unknown
        """ QWorkspace.windowActivated[QWidget] [signal] """
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def windowList(self, QWorkspace_WindowOrder_order=None): # real signature unknown; restored from __doc__
        """ QWorkspace.windowList(QWorkspace.WindowOrder order=QWorkspace.CreationOrder) -> list-of-QWidget """
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    CreationOrder = 0
    StackingOrder = 1


