# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsItem import QGraphicsItem

class QGraphicsPixmapItem(QGraphicsItem):
    """
    QGraphicsPixmapItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsPixmapItem(QPixmap, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.contains(QPointF) -> bool """
        return False

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.offset() -> QPointF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.pixmap() -> QPixmap """
        return QPixmap

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setOffset(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsPixmapItem.setOffset(QPointF)
        QGraphicsPixmapItem.setOffset(float, float)
        """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.setPixmap(QPixmap) """
        pass

    def setShapeMode(self, QGraphicsPixmapItem_ShapeMode): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.setShapeMode(QGraphicsPixmapItem.ShapeMode) """
        pass

    def setTransformationMode(self, Qt_TransformationMode): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.setTransformationMode(Qt.TransformationMode) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.shape() -> QPainterPath """
        return QPainterPath

    def shapeMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.shapeMode() -> QGraphicsPixmapItem.ShapeMode """
        pass

    def transformationMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.transformationMode() -> Qt.TransformationMode """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.type() -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BoundingRectShape = 1
    HeuristicMaskShape = 2
    MaskShape = 0


