# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QMenu(QWidget):
    """
    QMenu(QWidget parent=None)
    QMenu(QString, QWidget parent=None)
    """
    def aboutToHide(self, *args, **kwargs): # real signature unknown
        """ QMenu.aboutToHide [signal] """
        pass

    def aboutToShow(self, *args, **kwargs): # real signature unknown
        """ QMenu.aboutToShow [signal] """
        pass

    def actionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QMenu.actionAt(QPoint) -> QAction """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ QMenu.actionEvent(QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.actionGeometry(QAction) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ QMenu.activeAction() -> QAction """
        return QAction

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenu.addAction(QAction)
        QMenu.addAction(QString) -> QAction
        QMenu.addAction(QIcon, QString) -> QAction
        QMenu.addAction(QString, QObject, SLOT(), QKeySequence shortcut=0) -> QAction
        QMenu.addAction(QString, callable, QKeySequence shortcut=0) -> QAction
        QMenu.addAction(QIcon, QString, QObject, SLOT(), QKeySequence shortcut=0) -> QAction
        QMenu.addAction(QIcon, QString, callable, QKeySequence shortcut=0) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenu.addMenu(QMenu) -> QAction
        QMenu.addMenu(QString) -> QMenu
        QMenu.addMenu(QIcon, QString) -> QMenu
        """
        return QAction or QMenu

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ QMenu.addSeparator() -> QAction """
        return QAction

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QMenu.clear() """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QMenu.columnCount() -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ QMenu.defaultAction() -> QAction """
        return QAction

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

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.enterEvent(QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.event(QEvent) -> bool """
        return False

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenu.exec_() -> QAction
        QMenu.exec_(QPoint, QAction action=None) -> QAction
        QMenu.exec_(list-of-QAction, QPoint, QAction action=None) -> QAction
        QMenu.exec_(list-of-QAction, QPoint, QAction, QWidget) -> QAction
        """
        return QAction

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QMenu.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QMenu.hideEvent(QHideEvent) """
        pass

    def hideTearOffMenu(self): # real signature unknown; restored from __doc__
        """ QMenu.hideTearOffMenu() """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        """ QMenu.hovered[QAction] [signal] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QMenu.icon() -> QIcon """
        return QIcon

    def initStyleOption(self, QStyleOptionMenuItem, QAction): # real signature unknown; restored from __doc__
        """ QMenu.initStyleOption(QStyleOptionMenuItem, QAction) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertMenu(self, QAction, QMenu): # real signature unknown; restored from __doc__
        """ QMenu.insertMenu(QAction, QMenu) -> QAction """
        return QAction

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.insertSeparator(QAction) -> QAction """
        return QAction

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QMenu.isEmpty() -> bool """
        return False

    def isTearOffEnabled(self): # real signature unknown; restored from __doc__
        """ QMenu.isTearOffEnabled() -> bool """
        return False

    def isTearOffMenuVisible(self): # real signature unknown; restored from __doc__
        """ QMenu.isTearOffMenuVisible() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QMenu.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.leaveEvent(QEvent) """
        pass

    def menuAction(self): # real signature unknown; restored from __doc__
        """ QMenu.menuAction() -> QAction """
        return QAction

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenu.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenu.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenu.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QMenu.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def popup(self, QPoint, QAction_action=None): # real signature unknown; restored from __doc__
        """ QMenu.popup(QPoint, QAction action=None) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def separatorsCollapsible(self): # real signature unknown; restored from __doc__
        """ QMenu.separatorsCollapsible() -> bool """
        return False

    def setActiveAction(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.setActiveAction(QAction) """
        pass

    def setDefaultAction(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.setDefaultAction(QAction) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QMenu.setIcon(QIcon) """
        pass

    def setNoReplayFor(self, QWidget): # real signature unknown; restored from __doc__
        """ QMenu.setNoReplayFor(QWidget) """
        pass

    def setSeparatorsCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ QMenu.setSeparatorsCollapsible(bool) """
        pass

    def setTearOffEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QMenu.setTearOffEnabled(bool) """
        pass

    def setTitle(self, QString): # real signature unknown; restored from __doc__
        """ QMenu.setTitle(QString) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMenu.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QMenu.timerEvent(QTimerEvent) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QMenu.title() -> QString """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        """ QMenu.triggered[QAction] [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QMenu.wheelEvent(QWheelEvent) """
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


