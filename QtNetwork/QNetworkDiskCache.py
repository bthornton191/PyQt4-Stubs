# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractNetworkCache import QAbstractNetworkCache

class QNetworkDiskCache(QAbstractNetworkCache):
    """ QNetworkDiskCache(QObject parent=None) """
    def cacheDirectory(self): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.cacheDirectory() -> QString """
        pass

    def cacheSize(self): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.cacheSize() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.clear() """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.data(QUrl) -> QIODevice """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expire(self): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.expire() -> int """
        return 0

    def fileMetaData(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.fileMetaData(QString) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def insert(self, QIODevice): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.insert(QIODevice) """
        pass

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.maximumCacheSize() -> int """
        return 0

    def metaData(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.metaData(QUrl) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def prepare(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.prepare(QNetworkCacheMetaData) -> QIODevice """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.remove(QUrl) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCacheDirectory(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.setCacheDirectory(QString) """
        pass

    def setMaximumCacheSize(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.setMaximumCacheSize(int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMetaData(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ QNetworkDiskCache.updateMetaData(QNetworkCacheMetaData) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


