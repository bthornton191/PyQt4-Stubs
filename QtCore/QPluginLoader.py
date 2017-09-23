# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QPluginLoader(QObject):
    """
    QPluginLoader(QObject parent=None)
    QPluginLoader(QString, QObject parent=None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.errorString() -> QString """
        return QString

    def fileName(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.fileName() -> QString """
        return QString

    def instance(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.instance() -> QObject """
        return QObject

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.isLoaded() -> bool """
        return False

    def load(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.load() -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.loadHints() -> QLibrary.LoadHints """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QPluginLoader.setFileName(QString) """
        pass

    def setLoadHints(self, QLibrary_LoadHints): # real signature unknown; restored from __doc__
        """ QPluginLoader.setLoadHints(QLibrary.LoadHints) """
        pass

    def staticInstances(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.staticInstances() -> list-of-QObject """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.unload() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


