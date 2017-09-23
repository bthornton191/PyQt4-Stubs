# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerLua(QsciLexer):
    """ QsciLexerLua(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerLua.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerLua.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerLua.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerLua.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerLua.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerLua.foldCompact() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerLua.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerLua.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerLua.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerLua.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerLua.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerLua.setFoldCompact(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerLua.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    BasicFunctions = 13
    Character = 7
    Comment = 1
    CoroutinesIOSystemFacilities = 15
    Default = 0
    Identifier = 11
    Keyword = 5
    KeywordSet5 = 16
    KeywordSet6 = 17
    KeywordSet7 = 18
    KeywordSet8 = 19
    Label = 20
    LineComment = 2
    LiteralString = 8
    Number = 4
    Operator = 10
    Preprocessor = 9
    String = 6
    StringTableMathsFunctions = 14
    UnclosedString = 12


