# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
from typing import Type
import sip as __sip


from QObject import QObject
from .pyqtSignal import pyqtSignal

class QThread(QObject):
    """ QThread(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentThread(self): # real signature unknown; restored from __doc__
        """ QThread.currentThread() -> QThread """
        return QThread

    def currentThreadId(self): # real signature unknown; restored from __doc__
        """ QThread.currentThreadId() -> sip.voidptr """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ QThread.exec_() -> int """
        return 0

    def exit(self, int_returnCode=0): # real signature unknown; restored from __doc__
        """ QThread.exit(int returnCode=0) """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ QThread.finished [signal] """
        pass

    def idealThreadCount(self): # real signature unknown; restored from __doc__
        """ QThread.idealThreadCount() -> int """
        return 0

    def isFinished(self): # real signature unknown; restored from __doc__
        """ QThread.isFinished() -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ QThread.isRunning() -> bool """
        return False

    def msleep(self, p_int): # real signature unknown; restored from __doc__
        """ QThread.msleep(int) """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ QThread.priority() -> QThread.Priority """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ QThread.quit() """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ QThread.run() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPriority(self, QThread_Priority): # real signature unknown; restored from __doc__
        """ QThread.setPriority(QThread.Priority) """
        pass

    def setStackSize(self, p_int): # real signature unknown; restored from __doc__
        """ QThread.setStackSize(int) """
        pass

    def setTerminationEnabled(self, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QThread.setTerminationEnabled(bool enabled=True) """
        pass

    def sleep(self, p_int): # real signature unknown; restored from __doc__
        """ QThread.sleep(int) """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ QThread.stackSize() -> int """
        return 0

    def start(self, QThread_Priority_priority=None): # real signature unknown; restored from __doc__
        """ QThread.start(QThread.Priority priority=QThread.InheritPriority) """
        pass
    
    started: Type[pyqtSignal]
    # def started(self, *args, **kwargs): # real signature unknown
    #     """ QThread.started [signal] """
    #     pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ QThread.terminate() """
        pass

    def terminated(self, *args, **kwargs): # real signature unknown
        """ QThread.terminated [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def usleep(self, p_int): # real signature unknown; restored from __doc__
        """ QThread.usleep(int) """
        pass

    def wait(self, int_msecs=None): # real signature unknown; restored from __doc__
        """ QThread.wait(int msecs=ULONG_MAX) -> bool """
        return False

    def yieldCurrentThread(self): # real signature unknown; restored from __doc__
        """ QThread.yieldCurrentThread() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    HighestPriority = 5
    HighPriority = 4
    IdlePriority = 0
    InheritPriority = 7
    LowestPriority = 1
    LowPriority = 2
    NormalPriority = 3
    TimeCriticalPriority = 6


