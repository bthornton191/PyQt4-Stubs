# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerVHDL(QsciLexer):
    """ QsciLexerVHDL(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldAtBegin(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.foldAtBegin() -> bool """
        return False

    def foldAtElse(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.foldAtElse() -> bool """
        return False

    def foldAtParenthesis(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.foldAtParenthesis() -> bool """
        return False

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.foldCompact() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldAtBegin(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.setFoldAtBegin(bool) """
        pass

    def setFoldAtElse(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.setFoldAtElse(bool) """
        pass

    def setFoldAtParenthesis(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.setFoldAtParenthesis(bool) """
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.setFoldCompact(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerVHDL.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Attribute = 10
    Comment = 1
    CommentLine = 2
    Default = 0
    Identifier = 6
    Keyword = 8
    KeywordSet7 = 14
    Number = 3
    Operator = 5
    StandardFunction = 11
    StandardOperator = 9
    StandardPackage = 12
    StandardType = 13
    String = 4
    UnclosedString = 7


