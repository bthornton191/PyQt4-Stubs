# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QFrame import QFrame

class QSplitter(QFrame):
    """
    QSplitter(QWidget parent=None)
    QSplitter(Qt.Orientation, QWidget parent=None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QSplitter.addWidget(QWidget) """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QSplitter.changeEvent(QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QSplitter.childEvent(QChildEvent) """
        pass

    def childrenCollapsible(self): # real signature unknown; restored from __doc__
        """ QSplitter.childrenCollapsible() -> bool """
        return False

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closestLegalPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSplitter.closestLegalPosition(int, int) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QSplitter.count() -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createHandle(self): # real signature unknown; restored from __doc__
        """ QSplitter.createHandle() -> QSplitterHandle """
        return QSplitterHandle

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

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSplitter.event(QEvent) -> bool """
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

    def getRange(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.getRange(int) -> (int, int) """
        pass

    def handle(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.handle(int) -> QSplitterHandle """
        return QSplitterHandle

    def handleWidth(self): # real signature unknown; restored from __doc__
        """ QSplitter.handleWidth() -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QSplitter.indexOf(QWidget) -> int """
        return 0

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ QSplitter.insertWidget(int, QWidget) """
        pass

    def isCollapsible(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.isCollapsible(int) -> bool """
        return False

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

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QSplitter.minimumSizeHint() -> QSize """
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

    def moveSplitter(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSplitter.moveSplitter(int, int) """
        pass

    def opaqueResize(self): # real signature unknown; restored from __doc__
        """ QSplitter.opaqueResize() -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ QSplitter.orientation() -> Qt.Orientation """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ QSplitter.refresh() """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QSplitter.resizeEvent(QResizeEvent) """
        pass

    def restoreState(self, QByteArray): # real signature unknown; restored from __doc__
        """ QSplitter.restoreState(QByteArray) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ QSplitter.saveState() -> QByteArray """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setChildrenCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ QSplitter.setChildrenCollapsible(bool) """
        pass

    def setCollapsible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QSplitter.setCollapsible(int, bool) """
        pass

    def setHandleWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.setHandleWidth(int) """
        pass

    def setOpaqueResize(self, bool_opaque=True): # real signature unknown; restored from __doc__
        """ QSplitter.setOpaqueResize(bool opaque=True) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QSplitter.setOrientation(Qt.Orientation) """
        pass

    def setRubberBand(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.setRubberBand(int) """
        pass

    def setSizes(self, list_of_int): # real signature unknown; restored from __doc__
        """ QSplitter.setSizes(list-of-int) """
        pass

    def setStretchFactor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSplitter.setStretchFactor(int, int) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QSplitter.sizeHint() -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ QSplitter.sizes() -> list-of-int """
        pass

    def splitterMoved(self, *args, **kwargs): # real signature unknown
        """ QSplitter.splitterMoved[int, int] [signal] """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.widget(int) -> QWidget """
        return QWidget

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


