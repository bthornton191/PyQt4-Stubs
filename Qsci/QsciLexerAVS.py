# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerAVS(QsciLexer):
    """ QsciLexerAVS(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.defaultColor(int) -> QColor """
        pass

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.defaultFont(int) -> QFont """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.foldCompact() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.setFoldCompact(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerAVS.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    BlockComment = 1
    ClipProperty = 13
    Default = 0
    Filter = 10
    Function = 12
    Identifier = 6
    Keyword = 9
    KeywordSet6 = 14
    LineComment = 3
    NestedBlockComment = 2
    Number = 4
    Operator = 5
    Plugin = 11
    String = 7
    TripleString = 8


