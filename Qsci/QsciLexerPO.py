# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerPO(QsciLexer):
    """ QsciLexerPO(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPO.defaultColor(int) -> QColor """
        pass

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPO.defaultFont(int) -> QFont """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPO.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerPO.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerPO.foldCompact() -> bool """
        return False

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerPO.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerPO.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPO.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerPO.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPO.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPO.setFoldCompact(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPO.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Comment = 1
    Default = 0
    Flags = 11
    Fuzzy = 8
    MessageContext = 6
    MessageContextText = 7
    MessageContextTextEOL = 14
    MessageId = 2
    MessageIdText = 3
    MessageIdTextEOL = 12
    MessageString = 4
    MessageStringText = 5
    MessageStringTextEOL = 13
    ProgrammerComment = 9
    Reference = 10


