# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGraphicsEffect(__PyQt4_QtCore.QObject):
    """ QGraphicsEffect(QObject parent=None) """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.boundingRect() -> QRectF """
        pass

    def boundingRectFor(self, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.boundingRectFor(QRectF) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def draw(self, QPainter): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.draw(QPainter) """
        pass

    def drawSource(self, QPainter): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.drawSource(QPainter) """
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsEffect.enabledChanged[bool] [signal] """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.isEnabled() -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.setEnabled(bool) """
        pass

    def sourceBoundingRect(self, Qt_CoordinateSystem_system=None): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourceBoundingRect(Qt.CoordinateSystem system=Qt.LogicalCoordinates) -> QRectF """
        pass

    def sourceChanged(self, QGraphicsEffect_ChangeFlags): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourceChanged(QGraphicsEffect.ChangeFlags) """
        pass

    def sourceIsPixmap(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourceIsPixmap() -> bool """
        return False

    def sourcePixmap(self, Qt_CoordinateSystem_system=None, QGraphicsEffect_PixmapPadMode_mode=None): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourcePixmap(Qt.CoordinateSystem system=Qt.LogicalCoordinates, QGraphicsEffect.PixmapPadMode mode=QGraphicsEffect.PadToEffectiveBoundingRect) -> (QPixmap, QPoint) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.update() """
        pass

    def updateBoundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.updateBoundingRect() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    NoPad = 0
    PadToEffectiveBoundingRect = 2
    PadToTransparentBorder = 1
    SourceAttached = 1
    SourceBoundingRectChanged = 4
    SourceDetached = 2
    SourceInvalidated = 8


