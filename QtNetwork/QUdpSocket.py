# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractSocket import QAbstractSocket

class QUdpSocket(QAbstractSocket):
    """ QUdpSocket(QObject parent=None) """
    def bind(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.bind(QHostAddress, int) -> bool
        QUdpSocket.bind(int port=0) -> bool
        QUdpSocket.bind(QHostAddress, int, QUdpSocket.BindMode) -> bool
        QUdpSocket.bind(int, QUdpSocket.BindMode) -> bool
        """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingDatagrams(self): # real signature unknown; restored from __doc__
        """ QUdpSocket.hasPendingDatagrams() -> bool """
        return False

    def joinMulticastGroup(self, QHostAddress, QNetworkInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.joinMulticastGroup(QHostAddress) -> bool
        QUdpSocket.joinMulticastGroup(QHostAddress, QNetworkInterface) -> bool
        """
        return False

    def leaveMulticastGroup(self, QHostAddress, QNetworkInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.leaveMulticastGroup(QHostAddress) -> bool
        QUdpSocket.leaveMulticastGroup(QHostAddress, QNetworkInterface) -> bool
        """
        return False

    def multicastInterface(self): # real signature unknown; restored from __doc__
        """ QUdpSocket.multicastInterface() -> QNetworkInterface """
        return QNetworkInterface

    def pendingDatagramSize(self): # real signature unknown; restored from __doc__
        """ QUdpSocket.pendingDatagramSize() -> int """
        return 0

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readDatagram(self, p_int): # real signature unknown; restored from __doc__
        """ QUdpSocket.readDatagram(int) -> (str, QHostAddress, int) """
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setMulticastInterface(self, QNetworkInterface): # real signature unknown; restored from __doc__
        """ QUdpSocket.setMulticastInterface(QNetworkInterface) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def writeDatagram(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.writeDatagram(str, QHostAddress, int) -> int
        QUdpSocket.writeDatagram(QByteArray, QHostAddress, int) -> int
        """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    DefaultForPlatform = 0
    DontShareAddress = 2
    ReuseAddressHint = 4
    ShareAddress = 1


