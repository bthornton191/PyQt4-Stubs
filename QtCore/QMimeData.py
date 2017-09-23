# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QMimeData(QObject):
    """ QMimeData() """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QMimeData.clear() """
        pass

    def colorData(self): # real signature unknown; restored from __doc__
        """ QMimeData.colorData() -> QVariant """
        return QVariant

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.data(QString) -> QByteArray """
        return QByteArray

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def formats(self): # real signature unknown; restored from __doc__
        """ QMimeData.formats() -> QStringList """
        return QStringList

    def hasColor(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasColor() -> bool """
        return False

    def hasFormat(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.hasFormat(QString) -> bool """
        return False

    def hasHtml(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasHtml() -> bool """
        return False

    def hasImage(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasImage() -> bool """
        return False

    def hasText(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasText() -> bool """
        return False

    def hasUrls(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasUrls() -> bool """
        return False

    def html(self): # real signature unknown; restored from __doc__
        """ QMimeData.html() -> QString """
        return QString

    def imageData(self): # real signature unknown; restored from __doc__
        """ QMimeData.imageData() -> QVariant """
        return QVariant

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeFormat(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.removeFormat(QString) """
        pass

    def retrieveData(self, QString, Type): # real signature unknown; restored from __doc__
        """ QMimeData.retrieveData(QString, Type) -> QVariant """
        return QVariant

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColorData(self, QVariant): # real signature unknown; restored from __doc__
        """ QMimeData.setColorData(QVariant) """
        pass

    def setData(self, QString, QByteArray): # real signature unknown; restored from __doc__
        """ QMimeData.setData(QString, QByteArray) """
        pass

    def setHtml(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.setHtml(QString) """
        pass

    def setImageData(self, QVariant): # real signature unknown; restored from __doc__
        """ QMimeData.setImageData(QVariant) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.setText(QString) """
        pass

    def setUrls(self, list_of_QUrl): # real signature unknown; restored from __doc__
        """ QMimeData.setUrls(list-of-QUrl) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QMimeData.text() -> QString """
        return QString

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def urls(self): # real signature unknown; restored from __doc__
        """ QMimeData.urls() -> list-of-QUrl """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


