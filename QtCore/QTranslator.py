# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QTranslator(QObject):
    """ QTranslator(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QTranslator.isEmpty() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTranslator.load(QString, QString directory=QString(), QString searchDelimiters=QString(), QString suffix=QString()) -> bool
        QTranslator.load(QLocale, QString, QString prefix=QString(), QString directory=QString(), QString suffix=QString()) -> bool
        """
        pass

    def loadFromData(self, p_str): # real signature unknown; restored from __doc__
        """ QTranslator.loadFromData(str) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTranslator.translate(str, str, str disambiguation=None) -> QString
        QTranslator.translate(str, str, str, int) -> QString
        """
        return QString

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


