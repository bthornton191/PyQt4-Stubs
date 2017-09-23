# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QHttpHeader import QHttpHeader

class QHttpResponseHeader(QHttpHeader):
    """
    QHttpResponseHeader()
    QHttpResponseHeader(QHttpResponseHeader)
    QHttpResponseHeader(QString)
    QHttpResponseHeader(int, QString text=QString(), int major=1, int minor=1)
    """
    def majorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.majorVersion() -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.minorVersion() -> int """
        return 0

    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def parseLine(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.parseLine(QString, int) -> bool """
        return False

    def reasonPhrase(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.reasonPhrase() -> QString """
        pass

    def setStatusLine(self, p_int, QString_text=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHttpResponseHeader.setStatusLine(int, QString text=QString(), int major=1, int minor=1) """
        pass

    def setValid(self, *args, **kwargs): # real signature unknown
        pass

    def statusCode(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.statusCode() -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.toString() -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


