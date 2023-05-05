# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
from typing import Type
import PyQt4.QtCore as __PyQt4_QtCore


from .QWidget import QWidget
from .QAction import QAction
from ..QtCore.pyqtSignal import pyqtSignal

class QDockWidget(QWidget):
    """
    QDockWidget(QString, QWidget parent=None, Qt.WindowFlags flags=0)
    QDockWidget(QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ QDockWidget.allowedAreas() -> Qt.DockWidgetAreas """
        pass

    def allowedAreasChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.allowedAreasChanged[Qt.DockWidgetAreas] [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QDockWidget.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QDockWidget.closeEvent(QCloseEvent) """
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

    def dockLocationChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.dockLocationChanged[Qt.DockWidgetArea] [signal] """
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
        """ QDockWidget.event(QEvent) -> bool """
        return False

    def features(self): # real signature unknown; restored from __doc__
        """ QDockWidget.features() -> QDockWidget.DockWidgetFeatures """
        pass

    def featuresChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.featuresChanged[QDockWidget.DockWidgetFeatures] [signal] """
        pass

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

    def initStyleOption(self, QStyleOptionDockWidget): # real signature unknown; restored from __doc__
        """ QDockWidget.initStyleOption(QStyleOptionDockWidget) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isAreaAllowed(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ QDockWidget.isAreaAllowed(Qt.DockWidgetArea) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ QDockWidget.isFloating() -> bool """
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
        """ QDockWidget.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
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

    def setAllowedAreas(self, Qt_DockWidgetAreas): # real signature unknown; restored from __doc__
        """ QDockWidget.setAllowedAreas(Qt.DockWidgetAreas) """
        pass

    def setFeatures(self, QDockWidget_DockWidgetFeatures): # real signature unknown; restored from __doc__
        """ QDockWidget.setFeatures(QDockWidget.DockWidgetFeatures) """
        pass

    def setFloating(self, bool): # real signature unknown; restored from __doc__
        """ QDockWidget.setFloating(bool) """
        pass

    def setTitleBarWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDockWidget.setTitleBarWidget(QWidget) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDockWidget.setWidget(QWidget) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def titleBarWidget(self): # real signature unknown; restored from __doc__
        """ QDockWidget.titleBarWidget() -> QWidget """
        return QWidget

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ QDockWidget.toggleViewAction() -> QAction """
        return QAction

    def topLevelChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.topLevelChanged[bool] [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    visibilityChanged: Type[pyqtSignal]
    # def visibilityChanged(self, *args, **kwargs): # real signature unknown
    #     """ QDockWidget.visibilityChanged[bool] [signal] """
    #     pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ QDockWidget.widget() -> QWidget """
        return QWidget

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDockWidgetFeatures = 7
    DockWidgetClosable = 1
    DockWidgetFloatable = 4
    DockWidgetMovable = 2
    DockWidgetVerticalTitleBar = 8
    NoDockWidgetFeatures = 0


