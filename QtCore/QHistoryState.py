# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QAbstractState import QAbstractState

class QHistoryState(QAbstractState):
    """
    QHistoryState(QState parent=None)
    QHistoryState(QHistoryState.HistoryType, QState parent=None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultState(self): # real signature unknown; restored from __doc__
        """ QHistoryState.defaultState() -> QAbstractState """
        return QAbstractState

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QHistoryState.event(QEvent) -> bool """
        return False

    def historyType(self): # real signature unknown; restored from __doc__
        """ QHistoryState.historyType() -> QHistoryState.HistoryType """
        pass

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ QHistoryState.onEntry(QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ QHistoryState.onExit(QEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QHistoryState.setDefaultState(QAbstractState) """
        pass

    def setHistoryType(self, QHistoryState_HistoryType): # real signature unknown; restored from __doc__
        """ QHistoryState.setHistoryType(QHistoryState.HistoryType) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DeepHistory = 1
    ShallowHistory = 0


