# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractState(QObject):
    """ QAbstractState(QState parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def entered(self, *args, **kwargs): # real signature unknown
        """ QAbstractState.entered [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractState.event(QEvent) -> bool """
        return False

    def exited(self, *args, **kwargs): # real signature unknown
        """ QAbstractState.exited [signal] """
        pass

    def machine(self): # real signature unknown; restored from __doc__
        """ QAbstractState.machine() -> QStateMachine """
        return QStateMachine

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractState.onEntry(QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractState.onExit(QEvent) """
        pass

    def parentState(self): # real signature unknown; restored from __doc__
        """ QAbstractState.parentState() -> QState """
        return QState

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QState_parent=None): # real signature unknown; restored from __doc__
        pass


