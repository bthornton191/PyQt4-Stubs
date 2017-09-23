# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerCPP(QsciLexer):
    """ QsciLexerCPP(QObject parent=None, bool caseInsensitiveKeywords=False) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dollarsAllowed(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.dollarsAllowed() -> bool """
        return False

    def foldAtElse(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.foldAtElse() -> bool """
        return False

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.foldCompact() -> bool """
        return False

    def foldPreprocessor(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.foldPreprocessor() -> bool """
        return False

    def highlightHashQuotedStrings(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.highlightHashQuotedStrings() -> bool """
        return False

    def highlightTripleQuotedStrings(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.highlightTripleQuotedStrings() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDollarsAllowed(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setDollarsAllowed(bool) """
        pass

    def setFoldAtElse(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setFoldAtElse(bool) """
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setFoldCompact(bool) """
        pass

    def setFoldPreprocessor(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setFoldPreprocessor(bool) """
        pass

    def setHighlightHashQuotedStrings(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setHighlightHashQuotedStrings(bool) """
        pass

    def setHighlightTripleQuotedStrings(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setHighlightTripleQuotedStrings(bool) """
        pass

    def setStylePreprocessor(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.setStylePreprocessor(bool) """
        pass

    def stylePreprocessor(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.stylePreprocessor() -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerCPP.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None, bool_caseInsensitiveKeywords=False): # real signature unknown; restored from __doc__
        pass

    Comment = 1
    CommentDoc = 3
    CommentDocKeyword = 17
    CommentDocKeywordError = 18
    CommentLine = 2
    CommentLineDoc = 15
    Default = 0
    DoubleQuotedString = 6
    GlobalClass = 19
    HashQuotedString = 22
    Identifier = 11
    InactiveComment = 65
    InactiveCommentDoc = 67
    InactiveCommentDocKeyword = 81
    InactiveCommentDocKeywordError = 82
    InactiveCommentLine = 66
    InactiveCommentLineDoc = 79
    InactiveDefault = 64
    InactiveDoubleQuotedString = 70
    InactiveGlobalClass = 83
    InactiveHashQuotedString = 44
    InactiveIdentifier = 75
    InactiveKeyword = 69
    InactiveKeywordSet2 = 80
    InactiveNumber = 68
    InactiveOperator = 74
    InactivePreProcessor = 73
    InactivePreProcessorComment = 46
    InactivePreProcessorCommentLineDoc = 88
    InactiveRawString = 40
    InactiveRegex = 78
    InactiveSingleQuotedString = 71
    InactiveTripleQuotedVerbatimString = 42
    InactiveUnclosedString = 76
    InactiveUUID = 72
    InactiveVerbatimString = 77
    Keyword = 5
    KeywordSet2 = 16
    Number = 4
    Operator = 10
    PreProcessor = 9
    PreProcessorComment = 23
    PreProcessorCommentLineDoc = 24
    RawString = 20
    Regex = 14
    SingleQuotedString = 7
    TripleQuotedVerbatimString = 21
    UnclosedString = 12
    UUID = 8
    VerbatimString = 13


