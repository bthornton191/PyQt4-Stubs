# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerVerilog(QsciLexer):
    """ QsciLexerVerilog(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldAtElse(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.foldAtElse() -> bool """
        return False

    def foldAtModule(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.foldAtModule() -> bool """
        return False

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.foldCompact() -> bool """
        return False

    def foldPreprocessor(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.foldPreprocessor() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldAtElse(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.setFoldAtElse(bool) """
        pass

    def setFoldAtModule(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.setFoldAtModule(bool) """
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.setFoldCompact(bool) """
        pass

    def setFoldPreprocessor(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.setFoldPreprocessor(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerVerilog.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Comment = 1
    CommentBang = 3
    CommentLine = 2
    Default = 0
    Identifier = 11
    Keyword = 5
    KeywordSet2 = 7
    Number = 4
    Operator = 10
    Preprocessor = 9
    String = 6
    SystemTask = 8
    UnclosedString = 12
    UserKeywordSet = 19


