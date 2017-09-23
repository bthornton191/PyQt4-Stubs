# encoding: utf-8
# module PyQt4.QAxContainer
# from C:\Python27\lib\site-packages\PyQt4\QAxContainer.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QAxBase(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def asVariant(self): # real signature unknown; restored from __doc__
        """ QAxBase.asVariant() -> QVariant """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QAxBase.clear() """
        pass

    def control(self): # real signature unknown; restored from __doc__
        """ QAxBase.control() -> QString """
        pass

    def disableClassInfo(self): # real signature unknown; restored from __doc__
        """ QAxBase.disableClassInfo() """
        pass

    def disableEventSink(self): # real signature unknown; restored from __doc__
        """ QAxBase.disableEventSink() """
        pass

    def disableMetaObject(self): # real signature unknown; restored from __doc__
        """ QAxBase.disableMetaObject() """
        pass

    def dynamicCall(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAxBase.dynamicCall(str, list-of-QVariant) -> QVariant
        QAxBase.dynamicCall(str, QVariant value1=QVariant(), QVariant value2=QVariant(), QVariant value3=QVariant(), QVariant value4=QVariant(), QVariant value5=QVariant(), QVariant value6=QVariant(), QVariant value7=QVariant(), QVariant value8=QVariant()) -> QVariant
        """
        pass

    def generateDocumentation(self): # real signature unknown; restored from __doc__
        """ QAxBase.generateDocumentation() -> QString """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ QAxBase.isNull() -> bool """
        return False

    def propertyBag(self): # real signature unknown; restored from __doc__
        """ QAxBase.propertyBag() -> dict-of-QString-QVariant """
        pass

    def propertyWritable(self, p_str): # real signature unknown; restored from __doc__
        """ QAxBase.propertyWritable(str) -> bool """
        return False

    def querySubObject(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAxBase.querySubObject(str, list-of-QVariant) -> QAxObject
        QAxBase.querySubObject(str, QVariant value1=QVariant(), QVariant value2=QVariant(), QVariant value3=QVariant(), QVariant value4=QVariant(), QVariant value5=QVariant(), QVariant value6=QVariant(), QVariant value7=QVariant(), QVariant value8=QVariant()) -> QAxObject
        """
        return QAxObject

    def setControl(self, QString): # real signature unknown; restored from __doc__
        """ QAxBase.setControl(QString) -> bool """
        return False

    def setPropertyBag(self, dict_of_QString_QVariant): # real signature unknown; restored from __doc__
        """ QAxBase.setPropertyBag(dict-of-QString-QVariant) """
        pass

    def setPropertyWritable(self, p_str, bool): # real signature unknown; restored from __doc__
        """ QAxBase.setPropertyWritable(str, bool) """
        pass

    def verbs(self): # real signature unknown; restored from __doc__
        """ QAxBase.verbs() -> QStringList """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAxObject(__PyQt4_QtCore.QObject, QAxBase):
    """
    QAxObject(QObject parent=None)
    QAxObject(QString, QObject parent=None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, p_str): # real signature unknown; restored from __doc__
        """ QAxObject.connectNotify(str) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, QString): # real signature unknown; restored from __doc__
        """ QAxObject.doVerb(QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QAxWidget(__PyQt4_QtGui.QWidget, QAxBase):
    """
    QAxWidget(QWidget parent=None, Qt.WindowFlags flags=0)
    QAxWidget(QString, QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QAxWidget.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QAxWidget.clear() """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, p_str): # real signature unknown; restored from __doc__
        """ QAxWidget.connectNotify(str) """
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createHostWindow(self, bool): # real signature unknown; restored from __doc__
        """ QAxWidget.createHostWindow(bool) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, QString): # real signature unknown; restored from __doc__
        """ QAxWidget.doVerb(QString) -> bool """
        return False

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

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QAxWidget.minimumSizeHint() -> QSize """
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

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QAxWidget.resizeEvent(QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QAxWidget.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translateKeyEvent(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAxWidget.translateKeyEvent(int, int) -> bool """
        return False

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


