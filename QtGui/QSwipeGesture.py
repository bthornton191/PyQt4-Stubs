# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGesture import QGesture

class QSwipeGesture(QGesture):
    """ QSwipeGesture(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalDirection(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.horizontalDirection() -> QSwipeGesture.SwipeDirection """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setSwipeAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QSwipeGesture.setSwipeAngle(float) """
        pass

    def swipeAngle(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.swipeAngle() -> float """
        return 0.0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalDirection(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.verticalDirection() -> QSwipeGesture.SwipeDirection """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Down = 4
    Left = 1
    NoDirection = 0
    Right = 2
    Up = 3


