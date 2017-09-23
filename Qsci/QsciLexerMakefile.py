# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerMakefile(QsciLexer):
    """ QsciLexerMakefile(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.lexer() -> str """
        return ""

    def readProperties(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerMakefile.wordCharacters() -> str """
        return ""

    def writeProperties(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Comment = 1
    Default = 0
    Error = 9
    Operator = 4
    Preprocessor = 2
    Target = 5
    Variable = 3


