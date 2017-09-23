# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerPerl(QsciLexer):
    """ QsciLexerPerl(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldAtElse(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.foldAtElse() -> bool """
        return False

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.foldCompact() -> bool """
        return False

    def foldPackages(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.foldPackages() -> bool """
        return False

    def foldPODBlocks(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.foldPODBlocks() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldAtElse(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.setFoldAtElse(bool) """
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.setFoldCompact(bool) """
        pass

    def setFoldPackages(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.setFoldPackages(bool) """
        pass

    def setFoldPODBlocks(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.setFoldPODBlocks(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPerl.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Array = 13
    BacktickHereDocument = 25
    BacktickHereDocumentVar = 62
    Backticks = 20
    BackticksVar = 57
    Comment = 2
    DataSection = 21
    Default = 0
    DoubleQuotedHereDocument = 24
    DoubleQuotedHereDocumentVar = 61
    DoubleQuotedString = 6
    DoubleQuotedStringVar = 43
    Error = 1
    FormatBody = 42
    FormatIdentifier = 41
    Hash = 14
    HereDocumentDelimiter = 22
    Identifier = 11
    Keyword = 5
    Number = 4
    Operator = 10
    POD = 3
    PODVerbatim = 31
    QuotedStringQ = 26
    QuotedStringQQ = 27
    QuotedStringQQVar = 64
    QuotedStringQR = 29
    QuotedStringQRVar = 66
    QuotedStringQW = 30
    QuotedStringQX = 28
    QuotedStringQXVar = 65
    Regex = 17
    RegexVar = 54
    Scalar = 12
    SingleQuotedHereDocument = 23
    SingleQuotedString = 7
    SubroutinePrototype = 40
    Substitution = 18
    SubstitutionVar = 55
    SymbolTable = 15
    Translation = 44


