# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciLexer import QsciLexer

class QsciLexerCSS(QsciLexer):
    """ QsciLexerCSS(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.defaultColor(int) -> QColor """
        pass

    def defaultFont(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.defaultFont(int) -> QFont """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def foldComments(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.foldComments() -> bool """
        return False

    def foldCompact(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.foldCompact() -> bool """
        return False

    def HSSLanguage(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.HSSLanguage() -> bool """
        return False

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.language() -> str """
        return ""

    def LessLanguage(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.LessLanguage() -> bool """
        return False

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.lexer() -> str """
        return ""

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.readProperties(QSettings, QString) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.refreshProperties() """
        pass

    def SCSSLanguage(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.SCSSLanguage() -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFoldComments(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.setFoldComments(bool) """
        pass

    def setFoldCompact(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.setFoldCompact(bool) """
        pass

    def setHSSLanguage(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.setHSSLanguage(bool) """
        pass

    def setLessLanguage(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.setLessLanguage(bool) """
        pass

    def setSCSSLanguage(self, bool): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.setSCSSLanguage(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexerCSS.writeProperties(QSettings, QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    AtRule = 12
    Attribute = 16
    ClassSelector = 2
    Comment = 9
    CSS1Property = 6
    CSS2Property = 15
    CSS3Property = 17
    Default = 0
    DoubleQuotedString = 13
    ExtendedCSSProperty = 19
    ExtendedPseudoClass = 20
    ExtendedPseudoElement = 21
    IDSelector = 10
    Important = 11
    MediaRule = 22
    Operator = 5
    PseudoClass = 3
    PseudoElement = 18
    SingleQuotedString = 14
    Tag = 1
    UnknownProperty = 7
    UnknownPseudoClass = 4
    Value = 8
    Variable = 23


