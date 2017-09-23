# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QMenuBar(QWidget):
    """ QMenuBar(QWidget parent=None) """
    def actionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QMenuBar.actionAt(QPoint) -> QAction """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.actionEvent(QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ QMenuBar.actionGeometry(QAction) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ QMenuBar.activeAction() -> QAction """
        return QAction

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenuBar.addAction(QAction)
        QMenuBar.addAction(QString) -> QAction
        QMenuBar.addAction(QString, QObject, SLOT()) -> QAction
        QMenuBar.addAction(QString, callable) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenuBar.addMenu(QMenu) -> QAction
        QMenuBar.addMenu(QString) -> QMenu
        QMenuBar.addMenu(QIcon, QString) -> QMenu
        """
        return QAction or QMenu

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ QMenuBar.addSeparator() -> QAction """
        return QAction

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QMenuBar.clear() """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cornerWidget(self, Qt_Corner_corner=None): # real signature unknown; restored from __doc__
        """ QMenuBar.cornerWidget(Qt.Corner corner=Qt.TopRightCorner) -> QWidget """
        return QWidget

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
        """ QMenuBar.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.eventFilter(QObject, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.focusInEvent(QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.focusOutEvent(QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QMenuBar.heightForWidth(int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        """ QMenuBar.hovered[QAction] [signal] """
        pass

    def initStyleOption(self, QStyleOptionMenuItem, QAction): # real signature unknown; restored from __doc__
        """ QMenuBar.initStyleOption(QStyleOptionMenuItem, QAction) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertMenu(self, QAction, QMenu): # real signature unknown; restored from __doc__
        """ QMenuBar.insertMenu(QAction, QMenu) -> QAction """
        return QAction

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ QMenuBar.insertSeparator(QAction) -> QAction """
        return QAction

    def isDefaultUp(self): # real signature unknown; restored from __doc__
        """ QMenuBar.isDefaultUp() -> bool """
        return False

    def isNativeMenuBar(self): # real signature unknown; restored from __doc__
        """ QMenuBar.isNativeMenuBar() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.leaveEvent(QEvent) """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QMenuBar.minimumSizeHint() -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.resizeEvent(QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveAction(self, QAction): # real signature unknown; restored from __doc__
        """ QMenuBar.setActiveAction(QAction) """
        pass

    def setCornerWidget(self, QWidget, Qt_Corner_corner=None): # real signature unknown; restored from __doc__
        """ QMenuBar.setCornerWidget(QWidget, Qt.Corner corner=Qt.TopRightCorner) """
        pass

    def setDefaultUp(self, bool): # real signature unknown; restored from __doc__
        """ QMenuBar.setDefaultUp(bool) """
        pass

    def setNativeMenuBar(self, bool): # real signature unknown; restored from __doc__
        """ QMenuBar.setNativeMenuBar(bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QMenuBar.setVisible(bool) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMenuBar.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QMenuBar.timerEvent(QTimerEvent) """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        """ QMenuBar.triggered[QAction] [signal] """
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


