# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


class QsciLexer(__PyQt4_QtCore.QObject):
    """ QsciLexer(QObject parent=None) """
    def apis(self): # real signature unknown; restored from __doc__
        """ QsciLexer.apis() -> QsciAbstractAPIs """
        return QsciAbstractAPIs

    def autoIndentStyle(self): # real signature unknown; restored from __doc__
        """ QsciLexer.autoIndentStyle() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def color(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.color(int) -> QColor """
        pass

    def colorChanged(self, *args, **kwargs): # real signature unknown
        """ QsciLexer.colorChanged[QColor, int] [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultColor(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciLexer.defaultColor() -> QColor
        QsciLexer.defaultColor(int) -> QColor
        """
        pass

    def defaultEolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.defaultEolFill(int) -> bool """
        return False

    def defaultFont(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciLexer.defaultFont() -> QFont
        QsciLexer.defaultFont(int) -> QFont
        """
        pass

    def defaultPaper(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciLexer.defaultPaper() -> QColor
        QsciLexer.defaultPaper(int) -> QColor
        """
        pass

    def description(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.description(int) -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def editor(self): # real signature unknown; restored from __doc__
        """ QsciLexer.editor() -> QsciScintilla """
        return QsciScintilla

    def eolFill(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.eolFill(int) -> bool """
        return False

    def eolFillChanged(self, *args, **kwargs): # real signature unknown
        """ QsciLexer.eolFillChanged[bool, int] [signal] """
        pass

    def font(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.font(int) -> QFont """
        pass

    def fontChanged(self, *args, **kwargs): # real signature unknown
        """ QsciLexer.fontChanged[QFont, int] [signal] """
        pass

    def keywords(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.keywords(int) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ QsciLexer.language() -> str """
        return ""

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciLexer.lexer() -> str """
        return ""

    def lexerId(self): # real signature unknown; restored from __doc__
        """ QsciLexer.lexerId() -> int """
        return 0

    def paper(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.paper(int) -> QColor """
        pass

    def paperChanged(self, *args, **kwargs): # real signature unknown
        """ QsciLexer.paperChanged[QColor, int] [signal] """
        pass

    def propertyChanged(self, *args, **kwargs): # real signature unknown
        """ QsciLexer.propertyChanged[str, str] [signal] """
        pass

    def readProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexer.readProperties(QSettings, QString) -> bool """
        return False

    def readSettings(self, QSettings, str_prefix=None): # real signature unknown; restored from __doc__
        """ QsciLexer.readSettings(QSettings, str prefix="/Scintilla") -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshProperties(self): # real signature unknown; restored from __doc__
        """ QsciLexer.refreshProperties() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAPIs(self, QsciAbstractAPIs): # real signature unknown; restored from __doc__
        """ QsciLexer.setAPIs(QsciAbstractAPIs) """
        pass

    def setAutoIndentStyle(self, p_int): # real signature unknown; restored from __doc__
        """ QsciLexer.setAutoIndentStyle(int) """
        pass

    def setColor(self, QColor, int_style=-1): # real signature unknown; restored from __doc__
        """ QsciLexer.setColor(QColor, int style=-1) """
        pass

    def setDefaultColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciLexer.setDefaultColor(QColor) """
        pass

    def setDefaultFont(self, QFont): # real signature unknown; restored from __doc__
        """ QsciLexer.setDefaultFont(QFont) """
        pass

    def setDefaultPaper(self, QColor): # real signature unknown; restored from __doc__
        """ QsciLexer.setDefaultPaper(QColor) """
        pass

    def setEolFill(self, bool, int_style=-1): # real signature unknown; restored from __doc__
        """ QsciLexer.setEolFill(bool, int style=-1) """
        pass

    def setFont(self, QFont, int_style=-1): # real signature unknown; restored from __doc__
        """ QsciLexer.setFont(QFont, int style=-1) """
        pass

    def setPaper(self, QColor, int_style=-1): # real signature unknown; restored from __doc__
        """ QsciLexer.setPaper(QColor, int style=-1) """
        pass

    def styleBitsNeeded(self): # real signature unknown; restored from __doc__
        """ QsciLexer.styleBitsNeeded() -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciLexer.wordCharacters() -> str """
        return ""

    def writeProperties(self, QSettings, QString): # real signature unknown; restored from __doc__
        """ QsciLexer.writeProperties(QSettings, QString) -> bool """
        return False

    def writeSettings(self, QSettings, str_prefix=None): # real signature unknown; restored from __doc__
        """ QsciLexer.writeSettings(QSettings, str prefix="/Scintilla") -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


