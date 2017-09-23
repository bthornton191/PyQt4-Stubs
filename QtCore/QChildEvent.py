# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QEvent import QEvent

class QChildEvent(QEvent):
    """
    QChildEvent(QEvent.Type, QObject)
    QChildEvent(QChildEvent)
    """
    def added(self): # real signature unknown; restored from __doc__
        """ QChildEvent.added() -> bool """
        return False

    def child(self): # real signature unknown; restored from __doc__
        """ QChildEvent.child() -> QObject """
        return QObject

    def polished(self): # real signature unknown; restored from __doc__
        """ QChildEvent.polished() -> bool """
        return False

    def removed(self): # real signature unknown; restored from __doc__
        """ QChildEvent.removed() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


