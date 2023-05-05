# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
from typing import Type
import sip as __sip


from QObject import QObject
from pyqtSignal import pyqtSignal

class QTimer(QObject):
    """ QTimer(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def interval(self): # real signature unknown; restored from __doc__
        """ QTimer.interval() -> int """
        return 0

    def isActive(self): # real signature unknown; restored from __doc__
        """ QTimer.isActive() -> bool """
        return False

    def isSingleShot(self): # real signature unknown; restored from __doc__
        """ QTimer.isSingleShot() -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QTimer.setInterval(int) """
        pass

    def setSingleShot(self, bool): # real signature unknown; restored from __doc__
        """ QTimer.setSingleShot(bool) """
        pass

    @staticmethod
    def singleShot(p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTimer.singleShot(int, QObject, SLOT())
        QTimer.singleShot(int, callable)
        """
        pass

    def start(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTimer.start(int)
        QTimer.start()
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QTimer.stop() """
        pass

    timeout: Type[pyqtSignal]
    # def timeout(self, *args, **kwargs): # real signature unknown
    #     """ QTimer.timeout [signal] """
    #     pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QTimer.timerEvent(QTimerEvent) """
        pass

    def timerId(self): # real signature unknown; restored from __doc__
        """ QTimer.timerId() -> int """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


