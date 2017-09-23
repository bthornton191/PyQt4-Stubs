# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerMatlab(QsciLexer):
    """ QsciLexerMatlab(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMatlab.defaultColor(int) -> QColor """
        pass

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMatlab.defaultFont(int) -> QFont """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMatlab.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerMatlab.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerMatlab.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerMatlab.lexer() -> str """
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

    def writeProperties(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Command = 2
    Comment = 1
    Default = 0
    DoubleQuotedString = 8
    Identifier = 7
    Keyword = 4
    Number = 3
    Operator = 6
    SingleQuotedString = 5


