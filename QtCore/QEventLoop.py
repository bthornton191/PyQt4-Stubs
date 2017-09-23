# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QEventLoop(QObject):
    """ QEventLoop(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, QEventLoop_ProcessEventsFlags_flags=None): # real signature unknown; restored from __doc__
        """ QEventLoop.exec_(QEventLoop.ProcessEventsFlags flags=QEventLoop.AllEvents) -> int """
        return 0

    def exit(self, int_returnCode=0): # real signature unknown; restored from __doc__
        """ QEventLoop.exit(int returnCode=0) """
        pass

    def isRunning(self): # real signature unknown; restored from __doc__
        """ QEventLoop.isRunning() -> bool """
        return False

    def processEvents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QEventLoop.processEvents(QEventLoop.ProcessEventsFlags flags=QEventLoop.AllEvents) -> bool
        QEventLoop.processEvents(QEventLoop.ProcessEventsFlags, int)
        """
        return False

    def quit(self): # real signature unknown; restored from __doc__
        """ QEventLoop.quit() """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ QEventLoop.wakeUp() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    AllEvents = 0
    DeferredDeletion = 16
    ExcludeSocketNotifiers = 2
    ExcludeUserInputEvents = 1
    WaitForMoreEvents = 4
    X11ExcludeTimers = 8


