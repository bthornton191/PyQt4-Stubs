# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(QState sourceState=None)
    QEventTransition(QObject, QEvent.Type, QState sourceState=None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QEventTransition.event(QEvent) -> bool """
        return False

    def eventSource(self): # real signature unknown; restored from __doc__
        """ QEventTransition.eventSource() -> QObject """
        return QObject

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ QEventTransition.eventTest(QEvent) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ QEventTransition.eventType() -> QEvent.Type """
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ QEventTransition.onTransition(QEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventSource(self, QObject): # real signature unknown; restored from __doc__
        """ QEventTransition.setEventSource(QObject) """
        pass

    def setEventType(self, QEvent_Type): # real signature unknown; restored from __doc__
        """ QEventTransition.setEventType(QEvent.Type) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


