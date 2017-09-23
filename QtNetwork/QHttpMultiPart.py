# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHttpMultiPart(__PyQt4_QtCore.QObject):
    """
    QHttpMultiPart(QObject parent=None)
    QHttpMultiPart(QHttpMultiPart.ContentType, QObject parent=None)
    """
    def append(self, QHttpPart): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.append(QHttpPart) """
        pass

    def boundary(self): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.boundary() -> QByteArray """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBoundary(self, QByteArray): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.setBoundary(QByteArray) """
        pass

    def setContentType(self, QHttpMultiPart_ContentType): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.setContentType(QHttpMultiPart.ContentType) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlternativeType = 3
    FormDataType = 2
    MixedType = 0
    RelatedType = 1


