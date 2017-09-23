# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QMdiArea(QAbstractScrollArea):
    """ QMdiArea(QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activateNextSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activateNextSubWindow() """
        pass

    def activatePreviousSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activatePreviousSubWindow() """
        pass

    def activationOrder(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activationOrder() -> QMdiArea.WindowOrder """
        pass

    def activeSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activeSubWindow() -> QMdiSubWindow """
        return QMdiSubWindow

    def addSubWindow(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QMdiArea.addSubWindow(QWidget, Qt.WindowFlags flags=0) -> QMdiSubWindow """
        return QMdiSubWindow

    def background(self): # real signature unknown; restored from __doc__
        """ QMdiArea.background() -> QBrush """
        return QBrush

    def cascadeSubWindows(self): # real signature unknown; restored from __doc__
        """ QMdiArea.cascadeSubWindows() """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.childEvent(QChildEvent) """
        pass

    def closeActiveSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.closeActiveSubWindow() """
        pass

    def closeAllSubWindows(self): # real signature unknown; restored from __doc__
        """ QMdiArea.closeAllSubWindows() """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.currentSubWindow() -> QMdiSubWindow """
        return QMdiSubWindow

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ QMdiArea.documentMode() -> bool """
        return False

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
        """ QMdiArea.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.eventFilter(QObject, QEvent) -> bool """
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
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

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QMdiArea.minimumSizeHint() -> QSize """
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
        """ QMdiArea.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeSubWindow(self, QWidget): # real signature unknown; restored from __doc__
        """ QMdiArea.removeSubWindow(QWidget) """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.resizeEvent(QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QMdiArea.scrollContentsBy(int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActivationOrder(self, QMdiArea_WindowOrder): # real signature unknown; restored from __doc__
        """ QMdiArea.setActivationOrder(QMdiArea.WindowOrder) """
        pass

    def setActiveSubWindow(self, QMdiSubWindow): # real signature unknown; restored from __doc__
        """ QMdiArea.setActiveSubWindow(QMdiSubWindow) """
        pass

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QMdiArea.setBackground(QBrush) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ QMdiArea.setDocumentMode(bool) """
        pass

    def setOption(self, QMdiArea_AreaOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QMdiArea.setOption(QMdiArea.AreaOption, bool on=True) """
        pass

    def setTabPosition(self, QTabWidget_TabPosition): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabPosition(QTabWidget.TabPosition) """
        pass

    def setTabsClosable(self, bool): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabsClosable(bool) """
        pass

    def setTabShape(self, QTabWidget_TabShape): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabShape(QTabWidget.TabShape) """
        pass

    def setTabsMovable(self, bool): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabsMovable(bool) """
        pass

    def setupViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ QMdiArea.setupViewport(QWidget) """
        pass

    def setViewMode(self, QMdiArea_ViewMode): # real signature unknown; restored from __doc__
        """ QMdiArea.setViewMode(QMdiArea.ViewMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMdiArea.sizeHint() -> QSize """
        pass

    def subWindowActivated(self, *args, **kwargs): # real signature unknown
        """ QMdiArea.subWindowActivated[QMdiSubWindow] [signal] """
        pass

    def subWindowList(self, QMdiArea_WindowOrder_order=None): # real signature unknown; restored from __doc__
        """ QMdiArea.subWindowList(QMdiArea.WindowOrder order=QMdiArea.CreationOrder) -> list-of-QMdiSubWindow """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabPosition() -> QTabWidget.TabPosition """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabsClosable() -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabShape() -> QTabWidget.TabShape """
        pass

    def tabsMovable(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabsMovable() -> bool """
        return False

    def testOption(self, QMdiArea_AreaOption): # real signature unknown; restored from __doc__
        """ QMdiArea.testOption(QMdiArea.AreaOption) -> bool """
        return False

    def tileSubWindows(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tileSubWindows() """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.timerEvent(QTimerEvent) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QMdiArea.viewMode() -> QMdiArea.ViewMode """
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.viewportEvent(QEvent) -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    ActivationHistoryOrder = 2
    CreationOrder = 0
    DontMaximizeSubWindowOnActivation = 1
    StackingOrder = 1
    SubWindowView = 0
    TabbedView = 1


