# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerPython(QsciLexer):
    """ QsciLexerPython(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPython.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPython.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPython.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPython.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPython.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.foldCompact() -> bool """
        return False

    def foldQuotes(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.foldQuotes() -> bool """
        return False

    def highlightSubidentifiers(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.highlightSubidentifiers() -> bool """
        return False

    def indentationWarning(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.indentationWarning() -> QsciLexerPython.IndentationWarning """
        pass

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPython.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPython.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setFoldCompact(bool) """
        pass

    def setFoldQuotes(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setFoldQuotes(bool) """
        pass

    def setHighlightSubidentifiers(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setHighlightSubidentifiers(bool) """
        pass

    def setIndentationWarning(self, QsciLexerPython_IndentationWarning): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setIndentationWarning(QsciLexerPython.IndentationWarning) """
        pass

    def setStringsOverNewlineAllowed(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setStringsOverNewlineAllowed(bool) """
        pass

    def setV2UnicodeAllowed(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setV2UnicodeAllowed(bool) """
        pass

    def setV3BinaryOctalAllowed(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setV3BinaryOctalAllowed(bool) """
        pass

    def setV3BytesAllowed(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPython.setV3BytesAllowed(bool) """
        pass

    def stringsOverNewlineAllowed(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.stringsOverNewlineAllowed() -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def v2UnicodeAllowed(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.v2UnicodeAllowed() -> bool """
        return False

    def v3BinaryOctalAllowed(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.v3BinaryOctalAllowed() -> bool """
        return False

    def v3BytesAllowed(self): # real signature unknown; restored from __doc__
        """ QsciLexerPython.v3BytesAllowed() -> bool """
        return False

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPython.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    ClassName = 8
    Comment = 1
    CommentBlock = 12
    Decorator = 15
    Default = 0
    DoubleQuotedString = 3
    FunctionMethodName = 9
    HighlightedIdentifier = 14
    Identifier = 11
    Inconsistent = 1
    Keyword = 5
    NoWarning = 0
    Number = 2
    Operator = 10
    SingleQuotedString = 4
    Spaces = 3
    Tabs = 4
    TabsAfterSpaces = 2
    TripleDoubleQuotedString = 7
    TripleSingleQuotedString = 6
    UnclosedString = 13


