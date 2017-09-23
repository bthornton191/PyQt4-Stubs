# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerTCL(QsciLexer):
    """ QsciLexerTCL(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.foldComments() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.setFoldComments(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerTCL.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Comment = 1
    CommentBlock = 21
    CommentBox = 20
    CommentLine = 2
    Default = 0
    ExpandKeyword = 11
    Identifier = 7
    ITCLKeyword = 14
    KeywordSet6 = 16
    KeywordSet7 = 17
    KeywordSet8 = 18
    KeywordSet9 = 19
    Modifier = 10
    Number = 3
    Operator = 6
    QuotedKeyword = 4
    QuotedString = 5
    Substitution = 8
    SubstitutionBrace = 9
    TCLKeyword = 12
    TkCommand = 15
    TkKeyword = 13


