# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QDrag(__PyQt4_QtCore.QObject):
    """ QDrag(QWidget) """
    def actionChanged(self, *args, **kwargs): # real signature unknown
        """ QDrag.actionChanged[Qt.DropAction] [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDrag.exec_(Qt.DropActions supportedActions=Qt.MoveAction) -> Qt.DropAction
        QDrag.exec_(Qt.DropActions, Qt.DropAction) -> Qt.DropAction
        """
        pass

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ QDrag.hotSpot() -> QPoint """
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ QDrag.mimeData() -> QMimeData """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ QDrag.pixmap() -> QPixmap """
        return QPixmap

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDragCursor(self, QPixmap, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QDrag.setDragCursor(QPixmap, Qt.DropAction) """
        pass

    def setHotSpot(self, QPoint): # real signature unknown; restored from __doc__
        """ QDrag.setHotSpot(QPoint) """
        pass

    def setMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ QDrag.setMimeData(QMimeData) """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QDrag.setPixmap(QPixmap) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ QDrag.source() -> QWidget """
        return QWidget

    def start(self, Qt_DropActions_supportedActions=None): # real signature unknown; restored from __doc__
        """ QDrag.start(Qt.DropActions supportedActions=Qt.CopyAction) -> Qt.DropAction """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ QDrag.target() -> QWidget """
        return QWidget

    def targetChanged(self, *args, **kwargs): # real signature unknown
        """ QDrag.targetChanged[QWidget] [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget): # real signature unknown; restored from __doc__
        pass


