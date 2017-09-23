# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QThreadPool(QObject):
    """ QThreadPool(QObject parent=None) """
    def activeThreadCount(self): # real signature unknown; restored from __doc__
        """ QThreadPool.activeThreadCount() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expiryTimeout(self): # real signature unknown; restored from __doc__
        """ QThreadPool.expiryTimeout() -> int """
        return 0

    def globalInstance(self): # real signature unknown; restored from __doc__
        """ QThreadPool.globalInstance() -> QThreadPool """
        return QThreadPool

    def maxThreadCount(self): # real signature unknown; restored from __doc__
        """ QThreadPool.maxThreadCount() -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseThread(self): # real signature unknown; restored from __doc__
        """ QThreadPool.releaseThread() """
        pass

    def reserveThread(self): # real signature unknown; restored from __doc__
        """ QThreadPool.reserveThread() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExpiryTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ QThreadPool.setExpiryTimeout(int) """
        pass

    def setMaxThreadCount(self, p_int): # real signature unknown; restored from __doc__
        """ QThreadPool.setMaxThreadCount(int) """
        pass

    @staticmethod
    def start(QRunnable, int_priority=0): # real signature unknown; restored from __doc__
        """ QThreadPool.start(QRunnable, int priority=0) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tryStart(self, QRunnable): # real signature unknown; restored from __doc__
        """ QThreadPool.tryStart(QRunnable) -> bool """
        return False

    def waitForDone(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QThreadPool.waitForDone()
        QThreadPool.waitForDone(int) -> bool
        """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


