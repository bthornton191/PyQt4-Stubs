# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from QFile import QFile

class QTemporaryFile(QFile):
    """
    QTemporaryFile()
    QTemporaryFile(QString)
    QTemporaryFile(QObject)
    QTemporaryFile(QString, QObject)
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.autoRemove() -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createLocalFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTemporaryFile.createLocalFile(QString) -> QTemporaryFile
        QTemporaryFile.createLocalFile(QFile) -> QTemporaryFile
        """
        return QTemporaryFile

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fileEngine(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileEngine() -> QAbstractFileEngine """
        return QAbstractFileEngine

    def fileName(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileName() -> QString """
        return QString

    def fileTemplate(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileTemplate() -> QString """
        return QString

    def open(self, QIODevice_OpenMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTemporaryFile.open() -> bool
        QTemporaryFile.open(QIODevice.OpenMode) -> bool
        """
        return False

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRemove(self, bool): # real signature unknown; restored from __doc__
        """ QTemporaryFile.setAutoRemove(bool) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFileTemplate(self, QString): # real signature unknown; restored from __doc__
        """ QTemporaryFile.setFileTemplate(QString) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


