# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSharedMemory(QObject):
    """
    QSharedMemory(QObject parent=None)
    QSharedMemory(QString, QObject parent=None)
    """
    def attach(self, QSharedMemory_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSharedMemory.attach(QSharedMemory.AccessMode mode=QSharedMemory.ReadWrite) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def constData(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.constData() -> sip.voidptr """
        pass

    def create(self, p_int, QSharedMemory_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSharedMemory.create(int, QSharedMemory.AccessMode mode=QSharedMemory.ReadWrite) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.data() -> sip.voidptr """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.detach() -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.error() -> QSharedMemory.SharedMemoryError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.errorString() -> QString """
        return QString

    def isAttached(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.isAttached() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.key() -> QString """
        return QString

    def lock(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.lock() -> bool """
        return False

    def nativeKey(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.nativeKey() -> QString """
        return QString

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setKey(self, QString): # real signature unknown; restored from __doc__
        """ QSharedMemory.setKey(QString) """
        pass

    def setNativeKey(self, QString): # real signature unknown; restored from __doc__
        """ QSharedMemory.setNativeKey(QString) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.size() -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.unlock() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlreadyExists = 4
    InvalidSize = 2
    KeyError = 3
    LockError = 6
    NoError = 0
    NotFound = 5
    OutOfResources = 7
    PermissionDenied = 1
    ReadOnly = 0
    ReadWrite = 1
    UnknownError = 8


