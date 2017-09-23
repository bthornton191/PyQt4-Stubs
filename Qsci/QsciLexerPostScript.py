# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerPostScript(QsciLexer):
    """ QsciLexerPostScript(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.defaultColor(int) -> QColor """
        pass

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldAtElse(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.foldAtElse() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.foldCompact() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.language() -> str """
        return ""

    def level(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.level() -> int """
        return 0

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldAtElse(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.setFoldAtElse(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.setFoldCompact(bool) """
        pass

    def setLevel(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.setLevel(int) """
        pass

    def setTokenize(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.setTokenize(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tokenize(self): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.tokenize() -> bool """
        return False

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPostScript.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    ArrayParenthesis = 9
    BadStringCharacter = 15
    Base85String = 14
    Comment = 1
    Default = 0
    DictionaryParenthesis = 10
    DSCComment = 2
    DSCCommentValue = 3
    HexString = 13
    ImmediateEvalLiteral = 8
    Keyword = 6
    Literal = 7
    Name = 5
    Number = 4
    ProcedureParenthesis = 11
    Text = 12


