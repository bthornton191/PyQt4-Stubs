# encoding: utf-8
# module PyQt4.QtSvg
# from C:\Python27\lib\site-packages\PyQt4\QtSvg.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QGraphicsSvgItem(__PyQt4_QtGui.QGraphicsObject):
    """
    QGraphicsSvgItem(QGraphicsItem parent=None)
    QGraphicsSvgItem(QString, QGraphicsItem parent=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.boundingRect() -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def elementId(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.elementId() -> QString """
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

    def isCachingEnabled(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.isCachingEnabled() -> bool """
        return False

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.maximumCacheSize() -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.renderer() -> QSvgRenderer """
        return QSvgRenderer

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCachingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setCachingEnabled(bool) """
        pass

    def setElementId(self, QString): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setElementId(QString) """
        pass

    def setMaximumCacheSize(self, QSize): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setMaximumCacheSize(QSize) """
        pass

    def setSharedRenderer(self, QSvgRenderer): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setSharedRenderer(QSvgRenderer) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.type() -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgGenerator(__PyQt4_QtGui.QPaintDevice):
    """ QSvgGenerator() """
    def description(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.description() -> QString """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.fileName() -> QString """
        pass

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QSvgGenerator.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.outputDevice() -> QIODevice """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.paintEngine() -> QPaintEngine """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.resolution() -> int """
        return 0

    def setDescription(self, QString): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setDescription(QString) """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setFileName(QString) """
        pass

    def setOutputDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setOutputDevice(QIODevice) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setResolution(int) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setSize(QSize) """
        pass

    def setTitle(self, QString): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setTitle(QString) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgGenerator.setViewBox(QRect)
        QSvgGenerator.setViewBox(QRectF)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.size() -> QSize """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.title() -> QString """
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.viewBox() -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.viewBoxF() -> QRectF """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QSvgRenderer(__PyQt4_QtCore.QObject):
    """
    QSvgRenderer(QObject parent=None)
    QSvgRenderer(QString, QObject parent=None)
    QSvgRenderer(QByteArray, QObject parent=None)
    QSvgRenderer(QXmlStreamReader, QObject parent=None)
    """
    def animated(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.animated() -> bool """
        return False

    def animationDuration(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.animationDuration() -> int """
        return 0

    def boundsOnElement(self, QString): # real signature unknown; restored from __doc__
        """ QSvgRenderer.boundsOnElement(QString) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.currentFrame() -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSize(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.defaultSize() -> QSize """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elementExists(self, QString): # real signature unknown; restored from __doc__
        """ QSvgRenderer.elementExists(QString) -> bool """
        return False

    def framesPerSecond(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.framesPerSecond() -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.isValid() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgRenderer.load(QString) -> bool
        QSvgRenderer.load(QByteArray) -> bool
        QSvgRenderer.load(QXmlStreamReader) -> bool
        """
        return False

    def matrixForElement(self, QString): # real signature unknown; restored from __doc__
        """ QSvgRenderer.matrixForElement(QString) -> QMatrix """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgRenderer.render(QPainter)
        QSvgRenderer.render(QPainter, QRectF)
        QSvgRenderer.render(QPainter, QString, QRectF bounds=QRectF())
        """
        pass

    def repaintNeeded(self, *args, **kwargs): # real signature unknown
        """ QSvgRenderer.repaintNeeded [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentFrame(self, p_int): # real signature unknown; restored from __doc__
        """ QSvgRenderer.setCurrentFrame(int) """
        pass

    def setFramesPerSecond(self, p_int): # real signature unknown; restored from __doc__
        """ QSvgRenderer.setFramesPerSecond(int) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgRenderer.setViewBox(QRect)
        QSvgRenderer.setViewBox(QRectF)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.viewBox() -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.viewBoxF() -> QRectF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgWidget(__PyQt4_QtGui.QWidget):
    """
    QSvgWidget(QWidget parent=None)
    QSvgWidget(QString, QWidget parent=None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
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

    def event(self, *args, **kwargs): # real signature unknown
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

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgWidget.load(QString)
        QSvgWidget.load(QByteArray)
        """
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
        """ QSvgWidget.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ QSvgWidget.renderer() -> QSvgRenderer """
        return QSvgRenderer

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QSvgWidget.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


