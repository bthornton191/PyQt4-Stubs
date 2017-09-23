# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerPOV(QsciLexer):
    """ QsciLexerPOV(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.defaultColor(int) -> QColor """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.defaultFont(int) -> QFont """
        pass

    def defaultPaper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.defaultPaper(int) -> QColor """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.foldCompact() -> bool """
        return False

    def foldDirectives(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.foldDirectives() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.setFoldCompact(bool) """
        pass

    def setFoldDirectives(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.setFoldDirectives(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerPOV.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    BadDirective = 9
    Comment = 1
    CommentLine = 2
    Default = 0
    Directive = 8
    Identifier = 5
    KeywordSet6 = 14
    KeywordSet7 = 15
    KeywordSet8 = 16
    Number = 3
    ObjectsCSGAppearance = 10
    Operator = 4
    PredefinedFunctions = 13
    PredefinedIdentifiers = 12
    String = 6
    TypesModifiersItems = 11
    UnclosedString = 7


