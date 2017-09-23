# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerCoffeeScript(QsciLexer):
    """ QsciLexerCoffeeScript(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dollarsAllowed(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.dollarsAllowed() -> bool """
        return False

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.foldCompact() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDollarsAllowed(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.setDollarsAllowed(bool) """
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.setFoldCompact(bool) """
        pass

    def setStylePreprocessor(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.setStylePreprocessor(bool) """
        pass

    def stylePreprocessor(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.stylePreprocessor() -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerCoffeeScript.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    BlockRegex = 23
    BlockRegexComment = 24
    Comment = 1
    CommentBlock = 22
    CommentDoc = 3
    CommentDocKeyword = 17
    CommentDocKeywordError = 18
    CommentLine = 2
    CommentLineDoc = 15
    Default = 0
    DoubleQuotedString = 6
    GlobalClass = 19
    Identifier = 11
    Keyword = 5
    KeywordSet2 = 16
    Number = 4
    Operator = 10
    PreProcessor = 9
    Regex = 14
    SingleQuotedString = 7
    UnclosedString = 12
    UUID = 8
    VerbatimString = 13


