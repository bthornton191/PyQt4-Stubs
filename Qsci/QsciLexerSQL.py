# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerSQL(QsciLexer):
    """ QsciLexerSQL(QObject parent=None) """
    def backslashEscapes(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.backslashEscapes() -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dottedWords(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.dottedWords() -> bool """
        return False

    def foldAtElse(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.foldAtElse() -> bool """
        return False

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.foldCompact() -> bool """
        return False

    def foldOnlyBegin(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.foldOnlyBegin() -> bool """
        return False

    def hashComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.hashComments() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.lexer() -> str """
        return ""

    def quotedIdentifiers(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.quotedIdentifiers() -> bool """
        return False

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBackslashEscapes(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setBackslashEscapes(bool) """
        pass

    def setDottedWords(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setDottedWords(bool) """
        pass

    def setFoldAtElse(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setFoldAtElse(bool) """
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setFoldCompact(bool) """
        pass

    def setFoldOnlyBegin(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setFoldOnlyBegin(bool) """
        pass

    def setHashComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setHashComments(bool) """
        pass

    def setQuotedIdentifiers(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.setQuotedIdentifiers(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerSQL.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Comment = 1
    CommentDoc = 3
    CommentDocKeyword = 17
    CommentDocKeywordError = 18
    CommentLine = 2
    CommentLineHash = 15
    Default = 0
    DoubleQuotedString = 6
    Identifier = 11
    Keyword = 5
    KeywordSet5 = 19
    KeywordSet6 = 20
    KeywordSet7 = 21
    KeywordSet8 = 22
    Number = 4
    Operator = 10
    PlusComment = 13
    PlusKeyword = 8
    PlusPrompt = 9
    QuotedIdentifier = 23
    SingleQuotedString = 7


