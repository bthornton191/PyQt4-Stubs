# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGesture import QGesture

class QPinchGesture(QGesture):
    """ QPinchGesture(QObject parent=None) """
    def centerPoint(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.centerPoint() -> QPointF """
        pass

    def changeFlags(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.changeFlags() -> QPinchGesture.ChangeFlags """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def lastCenterPoint(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.lastCenterPoint() -> QPointF """
        pass

    def lastRotationAngle(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.lastRotationAngle() -> float """
        return 0.0

    def lastScaleFactor(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.lastScaleFactor() -> float """
        return 0.0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rotationAngle(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.rotationAngle() -> float """
        return 0.0

    def scaleFactor(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.scaleFactor() -> float """
        return 0.0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCenterPoint(self, QPointF): # real signature unknown; restored from __doc__
        """ QPinchGesture.setCenterPoint(QPointF) """
        pass

    def setChangeFlags(self, QPinchGesture_ChangeFlags): # real signature unknown; restored from __doc__
        """ QPinchGesture.setChangeFlags(QPinchGesture.ChangeFlags) """
        pass

    def setLastCenterPoint(self, QPointF): # real signature unknown; restored from __doc__
        """ QPinchGesture.setLastCenterPoint(QPointF) """
        pass

    def setLastRotationAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QPinchGesture.setLastRotationAngle(float) """
        pass

    def setLastScaleFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QPinchGesture.setLastScaleFactor(float) """
        pass

    def setRotationAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QPinchGesture.setRotationAngle(float) """
        pass

    def setScaleFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QPinchGesture.setScaleFactor(float) """
        pass

    def setStartCenterPoint(self, QPointF): # real signature unknown; restored from __doc__
        """ QPinchGesture.setStartCenterPoint(QPointF) """
        pass

    def setTotalChangeFlags(self, QPinchGesture_ChangeFlags): # real signature unknown; restored from __doc__
        """ QPinchGesture.setTotalChangeFlags(QPinchGesture.ChangeFlags) """
        pass

    def setTotalRotationAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QPinchGesture.setTotalRotationAngle(float) """
        pass

    def setTotalScaleFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QPinchGesture.setTotalScaleFactor(float) """
        pass

    def startCenterPoint(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.startCenterPoint() -> QPointF """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalChangeFlags(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.totalChangeFlags() -> QPinchGesture.ChangeFlags """
        pass

    def totalRotationAngle(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.totalRotationAngle() -> float """
        return 0.0

    def totalScaleFactor(self): # real signature unknown; restored from __doc__
        """ QPinchGesture.totalScaleFactor() -> float """
        return 0.0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    CenterPointChanged = 4
    RotationAngleChanged = 2
    ScaleFactorChanged = 1


