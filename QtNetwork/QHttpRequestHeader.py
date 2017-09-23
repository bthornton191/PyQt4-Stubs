# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QHttpHeader import QHttpHeader

class QHttpRequestHeader(QHttpHeader):
    """
    QHttpRequestHeader()
    QHttpRequestHeader(QString, QString, int major=1, int minor=1)
    QHttpRequestHeader(QHttpRequestHeader)
    QHttpRequestHeader(QString)
    """
    def majorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.majorVersion() -> int """
        return 0

    def method(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.method() -> QString """
        pass

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.minorVersion() -> int """
        return 0

    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def parseLine(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.parseLine(QString, int) -> bool """
        return False

    def path(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.path() -> QString """
        pass

    def setRequest(self, QString, QString_1, int_major=1, int_minor=1): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.setRequest(QString, QString, int major=1, int minor=1) """
        pass

    def setValid(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.toString() -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


