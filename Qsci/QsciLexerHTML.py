# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerHTML(QsciLexer):
    """ QsciLexerHTML(QObject parent=None) """
    def caseSensitiveTags(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.caseSensitiveTags() -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def djangoTemplates(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.djangoTemplates() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.foldCompact() -> bool """
        return False

    def foldPreprocessor(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.foldPreprocessor() -> bool """
        return False

    def foldScriptComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.foldScriptComments() -> bool """
        return False

    def foldScriptHeredocs(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.foldScriptHeredocs() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.lexer() -> str """
        return ""

    def makoTemplates(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.makoTemplates() -> bool """
        return False

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCaseSensitiveTags(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setCaseSensitiveTags(bool) """
        pass

    def setDjangoTemplates(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setDjangoTemplates(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setFoldCompact(bool) """
        pass

    def setFoldPreprocessor(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setFoldPreprocessor(bool) """
        pass

    def setFoldScriptComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setFoldScriptComments(bool) """
        pass

    def setFoldScriptHeredocs(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setFoldScriptHeredocs(bool) """
        pass

    def setMakoTemplates(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.setMakoTemplates(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerHTML.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    ASPAtStart = 15
    ASPJavaScriptComment = 57
    ASPJavaScriptCommentDoc = 59
    ASPJavaScriptCommentLine = 58
    ASPJavaScriptDefault = 56
    ASPJavaScriptDoubleQuotedString = 63
    ASPJavaScriptKeyword = 62
    ASPJavaScriptNumber = 60
    ASPJavaScriptRegex = 67
    ASPJavaScriptSingleQuotedString = 64
    ASPJavaScriptStart = 55
    ASPJavaScriptSymbol = 65
    ASPJavaScriptUnclosedString = 66
    ASPJavaScriptWord = 61
    ASPPythonClassName = 114
    ASPPythonComment = 107
    ASPPythonDefault = 106
    ASPPythonDoubleQuotedString = 109
    ASPPythonFunctionMethodName = 115
    ASPPythonIdentifier = 117
    ASPPythonKeyword = 111
    ASPPythonNumber = 108
    ASPPythonOperator = 116
    ASPPythonSingleQuotedString = 110
    ASPPythonStart = 105
    ASPPythonTripleDoubleQuotedString = 113
    ASPPythonTripleSingleQuotedString = 112
    ASPStart = 16
    ASPVBScriptComment = 82
    ASPVBScriptDefault = 81
    ASPVBScriptIdentifier = 86
    ASPVBScriptKeyword = 84
    ASPVBScriptNumber = 83
    ASPVBScriptStart = 80
    ASPVBScriptString = 85
    ASPVBScriptUnclosedString = 87
    ASPXCComment = 20
    Attribute = 3
    CDATA = 17
    Default = 0
    Entity = 10
    HTMLComment = 9
    HTMLDoubleQuotedString = 6
    HTMLNumber = 5
    HTMLSingleQuotedString = 7
    HTMLValue = 19
    JavaScriptComment = 42
    JavaScriptCommentDoc = 44
    JavaScriptCommentLine = 43
    JavaScriptDefault = 41
    JavaScriptDoubleQuotedString = 48
    JavaScriptKeyword = 47
    JavaScriptNumber = 45
    JavaScriptRegex = 52
    JavaScriptSingleQuotedString = 49
    JavaScriptStart = 40
    JavaScriptSymbol = 50
    JavaScriptUnclosedString = 51
    JavaScriptWord = 46
    OtherInTag = 8
    PHPComment = 124
    PHPCommentLine = 125
    PHPDefault = 118
    PHPDoubleQuotedString = 119
    PHPDoubleQuotedVariable = 126
    PHPKeyword = 121
    PHPNumber = 122
    PHPOperator = 127
    PHPSingleQuotedString = 120
    PHPStart = 18
    PHPVariable = 123
    PythonClassName = 99
    PythonComment = 92
    PythonDefault = 91
    PythonDoubleQuotedString = 94
    PythonFunctionMethodName = 100
    PythonIdentifier = 102
    PythonKeyword = 96
    PythonNumber = 93
    PythonOperator = 101
    PythonSingleQuotedString = 95
    PythonStart = 90
    PythonTripleDoubleQuotedString = 98
    PythonTripleSingleQuotedString = 97
    Script = 14
    SGMLBlockDefault = 31
    SGMLCommand = 22
    SGMLComment = 29
    SGMLDefault = 21
    SGMLDoubleQuotedString = 24
    SGMLEntity = 28
    SGMLError = 26
    SGMLParameter = 23
    SGMLParameterComment = 30
    SGMLSingleQuotedString = 25
    SGMLSpecial = 27
    Tag = 1
    UnknownAttribute = 4
    UnknownTag = 2
    VBScriptComment = 72
    VBScriptDefault = 71
    VBScriptIdentifier = 76
    VBScriptKeyword = 74
    VBScriptNumber = 73
    VBScriptStart = 70
    VBScriptString = 75
    VBScriptUnclosedString = 77
    XMLEnd = 13
    XMLStart = 12
    XMLTagEnd = 11


