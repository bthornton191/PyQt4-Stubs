# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGesture(__PyQt4_QtCore.QObject):
    """ QGesture(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def gestureCancelPolicy(self): # real signature unknown; restored from __doc__
        """ QGesture.gestureCancelPolicy() -> QGesture.GestureCancelPolicy """
        pass

    def gestureType(self): # real signature unknown; restored from __doc__
        """ QGesture.gestureType() -> Qt.GestureType """
        pass

    def hasHotSpot(self): # real signature unknown; restored from __doc__
        """ QGesture.hasHotSpot() -> bool """
        return False

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ QGesture.hotSpot() -> QPointF """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setGestureCancelPolicy(self, QGesture_GestureCancelPolicy): # real signature unknown; restored from __doc__
        """ QGesture.setGestureCancelPolicy(QGesture.GestureCancelPolicy) """
        pass

    def setHotSpot(self, QPointF): # real signature unknown; restored from __doc__
        """ QGesture.setHotSpot(QPointF) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QGesture.state() -> Qt.GestureState """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unsetHotSpot(self): # real signature unknown; restored from __doc__
        """ QGesture.unsetHotSpot() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    CancelAllInContext = 1
    CancelNone = 0


