# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QFrame import QFrame

class QToolBox(QFrame):
    """ QToolBox(QWidget parent=None, Qt.WindowFlags flags=0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QToolBox.addItem(QWidget, QString) -> int
        QToolBox.addItem(QWidget, QIcon, QString) -> int
        """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QToolBox.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QToolBox.count() -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBox.currentChanged[int] [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QToolBox.currentIndex() -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ QToolBox.currentWidget() -> QWidget """
        return QWidget

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
        """ QToolBox.event(QEvent) -> bool """
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

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QToolBox.indexOf(QWidget) -> int """
        return 0

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertItem(self, p_int, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QToolBox.insertItem(int, QWidget, QString) -> int
        QToolBox.insertItem(int, QWidget, QIcon, QString) -> int
        """
        return 0

    def isItemEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.isItemEnabled(int) -> bool """
        return False

    def itemIcon(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemIcon(int) -> QIcon """
        return QIcon

    def itemInserted(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemInserted(int) """
        pass

    def itemRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemRemoved(int) """
        pass

    def itemText(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemText(int) -> QString """
        pass

    def itemToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemToolTip(int) -> QString """
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.removeItem(int) """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.setCurrentIndex(int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QToolBox.setCurrentWidget(QWidget) """
        pass

    def setItemEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QToolBox.setItemEnabled(int, bool) """
        pass

    def setItemIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QToolBox.setItemIcon(int, QIcon) """
        pass

    def setItemText(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QToolBox.setItemText(int, QString) """
        pass

    def setItemToolTip(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QToolBox.setItemToolTip(int, QString) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QToolBox.showEvent(QShowEvent) """
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
        """ QToolBox.widget(int) -> QWidget """
        return QWidget

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


