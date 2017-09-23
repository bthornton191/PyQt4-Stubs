# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAbstractNetworkCache(__PyQt4_QtCore.QObject):
    """ QAbstractNetworkCache(QObject parent=None) """
    def cacheSize(self): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.cacheSize() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.clear() """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QUrl): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.data(QUrl) -> QIODevice """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, QIODevice): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.insert(QIODevice) """
        pass

    def metaData(self, QUrl): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.metaData(QUrl) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def prepare(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.prepare(QNetworkCacheMetaData) -> QIODevice """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, QUrl): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.remove(QUrl) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMetaData(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.updateMetaData(QNetworkCacheMetaData) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


