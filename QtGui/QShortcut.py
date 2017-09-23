# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QShortcut(__PyQt4_QtCore.QObject):
    """
    QShortcut(QWidget)
    QShortcut(QKeySequence, QWidget, SLOT() member=0, SLOT() ambiguousMember=0, Qt.ShortcutContext context=Qt.WindowShortcut)
    """
    def activated(self, *args, **kwargs): # real signature unknown
        """ QShortcut.activated [signal] """
        pass

    def activatedAmbiguously(self, *args, **kwargs): # real signature unknown
        """ QShortcut.activatedAmbiguously [signal] """
        pass

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ QShortcut.autoRepeat() -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ QShortcut.context() -> Qt.ShortcutContext """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QShortcut.event(QEvent) -> bool """
        return False

    def id(self): # real signature unknown; restored from __doc__
        """ QShortcut.id() -> int """
        return 0

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QShortcut.isEnabled() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QShortcut.key() -> QKeySequence """
        return QKeySequence

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ QShortcut.parentWidget() -> QWidget """
        return QWidget

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRepeat(self, bool): # real signature unknown; restored from __doc__
        """ QShortcut.setAutoRepeat(bool) """
        pass

    def setContext(self, Qt_ShortcutContext): # real signature unknown; restored from __doc__
        """ QShortcut.setContext(Qt.ShortcutContext) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QShortcut.setEnabled(bool) """
        pass

    def setKey(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QShortcut.setKey(QKeySequence) """
        pass

    def setWhatsThis(self, QString): # real signature unknown; restored from __doc__
        """ QShortcut.setWhatsThis(QString) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QShortcut.whatsThis() -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


