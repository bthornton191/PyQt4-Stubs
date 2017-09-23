# encoding: utf-8
# module PyQt4.Qsci
# from C:\Python27\lib\site-packages\PyQt4\Qsci.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


from QsciScintillaBase import QsciScintillaBase

class QsciScintilla(QsciScintillaBase):
    """ QsciScintilla(QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def annotate(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.annotate(int, QString, int)
        QsciScintilla.annotate(int, QString, QsciStyle)
        QsciScintilla.annotate(int, QsciStyledText)
        QsciScintilla.annotate(int, list-of-QsciStyledText)
        """
        pass

    def annotation(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.annotation(int) -> QString """
        pass

    def annotationDisplay(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.annotationDisplay() -> QsciScintilla.AnnotationDisplay """
        pass

    def apiContext(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.apiContext(int) -> (QStringList, int, int) """
        pass

    def append(self, QString): # real signature unknown; restored from __doc__
        """ QsciScintilla.append(QString) """
        pass

    def autoCompleteFromAll(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompleteFromAll() """
        pass

    def autoCompleteFromAPIs(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompleteFromAPIs() """
        pass

    def autoCompleteFromDocument(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompleteFromDocument() """
        pass

    def autoCompletionCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionCaseSensitivity() -> bool """
        return False

    def autoCompletionFillupsEnabled(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionFillupsEnabled() -> bool """
        return False

    def autoCompletionReplaceWord(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionReplaceWord() -> bool """
        return False

    def autoCompletionShowSingle(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionShowSingle() -> bool """
        return False

    def autoCompletionSource(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionSource() -> QsciScintilla.AutoCompletionSource """
        pass

    def autoCompletionThreshold(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionThreshold() -> int """
        return 0

    def autoCompletionUseSingle(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoCompletionUseSingle() -> QsciScintilla.AutoCompletionUseSingle """
        pass

    def autoIndent(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.autoIndent() -> bool """
        return False

    def backspaceUnindents(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.backspaceUnindents() -> bool """
        return False

    def beginUndoAction(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.beginUndoAction() """
        pass

    def braceMatching(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.braceMatching() -> QsciScintilla.BraceMatch """
        pass

    def callTip(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.callTip() """
        pass

    def callTipsPosition(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.callTipsPosition() -> QsciScintilla.CallTipsPosition """
        pass

    def callTipsStyle(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.callTipsStyle() -> QsciScintilla.CallTipsStyle """
        pass

    def callTipsVisible(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.callTipsVisible() -> int """
        return 0

    def cancelList(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.cancelList() """
        pass

    def canInsertFromMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def caseSensitive(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.caseSensitive() -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QsciScintilla.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.clear() """
        pass

    def clearAnnotations(self, int_line=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.clearAnnotations(int line=-1) """
        pass

    def clearFolds(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.clearFolds() """
        pass

    def clearIndicatorRange(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4): # real signature unknown; restored from __doc__
        """ QsciScintilla.clearIndicatorRange(int, int, int, int, int) """
        pass

    def clearMarginText(self, int_line=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.clearMarginText(int line=-1) """
        pass

    def clearRegisteredImages(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.clearRegisteredImages() """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.color() -> QColor """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QsciScintilla.contextMenuEvent(QContextMenuEvent) """
        pass

    def contractedFolds(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.contractedFolds() -> list-of-int """
        pass

    def convertEols(self, QsciScintilla_EolMode): # real signature unknown; restored from __doc__
        """ QsciScintilla.convertEols(QsciScintilla.EolMode) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.copy() """
        pass

    def copyAvailable(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.copyAvailable[bool] [signal] """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.createStandardContextMenu() -> QMenu """
        pass

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.cursorPositionChanged[int, int] [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.cut() """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.document() -> QsciDocument """
        return QsciDocument

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def edgeColor(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.edgeColor() -> QColor """
        pass

    def edgeColumn(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.edgeColumn() -> int """
        return 0

    def edgeMode(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.edgeMode() -> QsciScintilla.EdgeMode """
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def endUndoAction(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.endUndoAction() """
        pass

    def ensureCursorVisible(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.ensureCursorVisible() """
        pass

    def ensureLineVisible(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.ensureLineVisible(int) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def eolMode(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.eolMode() -> QsciScintilla.EolMode """
        pass

    def eolVisibility(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.eolVisibility() -> bool """
        return False

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QsciScintilla.event(QEvent) -> bool """
        return False

    def extraAscent(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.extraAscent() -> int """
        return 0

    def extraDescent(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.extraDescent() -> int """
        return 0

    def fillIndicatorRange(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4): # real signature unknown; restored from __doc__
        """ QsciScintilla.fillIndicatorRange(int, int, int, int, int) """
        pass

    def findFirst(self, QString, bool, bool_1, bool_2, bool_3, bool_forward=True, int_line=-1, int_index=-1, bool_show=True, bool_posix=False): # real signature unknown; restored from __doc__
        """ QsciScintilla.findFirst(QString, bool, bool, bool, bool, bool forward=True, int line=-1, int index=-1, bool show=True, bool posix=False) -> bool """
        return False

    def findFirstInSelection(self, QString, bool, bool_1, bool_2, bool_forward=True, bool_show=True, bool_posix=False): # real signature unknown; restored from __doc__
        """ QsciScintilla.findFirstInSelection(QString, bool, bool, bool, bool forward=True, bool show=True, bool posix=False) -> bool """
        return False

    def findNext(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.findNext() -> bool """
        return False

    def firstVisibleLine(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.firstVisibleLine() -> int """
        return 0

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def foldAll(self, bool_children=False): # real signature unknown; restored from __doc__
        """ QsciScintilla.foldAll(bool children=False) """
        pass

    def folding(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.folding() -> QsciScintilla.FoldStyle """
        pass

    def foldLine(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.foldLine(int) """
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def fromMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def getCursorPosition(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.getCursorPosition() -> (int, int) """
        pass

    def getSelection(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.getSelection() -> (int, int, int, int) """
        pass

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.hasSelectedText() -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indent(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.indent(int) """
        pass

    def indentation(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.indentation(int) -> int """
        return 0

    def indentationGuides(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.indentationGuides() -> bool """
        return False

    def indentationsUseTabs(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.indentationsUseTabs() -> bool """
        return False

    def indentationWidth(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.indentationWidth() -> int """
        return 0

    def indicatorClicked(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.indicatorClicked[int, int, Qt.KeyboardModifiers] [signal] """
        pass

    def indicatorDefine(self, QsciScintilla_IndicatorStyle, int_indicatorNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.indicatorDefine(QsciScintilla.IndicatorStyle, int indicatorNumber=-1) -> int """
        return 0

    def indicatorDrawUnder(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.indicatorDrawUnder(int) -> bool """
        return False

    def indicatorReleased(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.indicatorReleased[int, int, Qt.KeyboardModifiers] [signal] """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, QString): # real signature unknown; restored from __doc__
        """ QsciScintilla.insert(QString) """
        pass

    def insertAt(self, QString, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.insertAt(QString, int, int) """
        pass

    def isCallTipActive(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isCallTipActive() -> bool """
        return False

    def isListActive(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isListActive() -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isModified() -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isReadOnly() -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isRedoAvailable() -> bool """
        return False

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isUndoAvailable() -> bool """
        return False

    def isUtf8(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.isUtf8() -> bool """
        return False

    def isWordCharacter(self, p_str): # real signature unknown; restored from __doc__
        """ QsciScintilla.isWordCharacter(str) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.length() -> int """
        return 0

    def lexer(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.lexer() -> QsciLexer """
        return QsciLexer

    def lineAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QsciScintilla.lineAt(QPoint) -> int """
        return 0

    def lineIndexFromPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.lineIndexFromPosition(int) -> (int, int) """
        pass

    def lineLength(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.lineLength(int) -> int """
        return 0

    def lines(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.lines() -> int """
        return 0

    def linesChanged(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.linesChanged [signal] """
        pass

    def marginClicked(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.marginClicked[int, int, Qt.KeyboardModifiers] [signal] """
        pass

    def marginLineNumbers(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.marginLineNumbers(int) -> bool """
        return False

    def marginMarkerMask(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.marginMarkerMask(int) -> int """
        return 0

    def marginOptions(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.marginOptions() -> int """
        return 0

    def marginSensitivity(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.marginSensitivity(int) -> bool """
        return False

    def marginType(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.marginType(int) -> QsciScintilla.MarginType """
        pass

    def marginWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.marginWidth(int) -> int """
        return 0

    def markerAdd(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerAdd(int, int) -> int """
        return 0

    def markerDefine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.markerDefine(QsciScintilla.MarkerSymbol, int markerNumber=-1) -> int
        QsciScintilla.markerDefine(str, int markerNumber=-1) -> int
        QsciScintilla.markerDefine(QPixmap, int markerNumber=-1) -> int
        QsciScintilla.markerDefine(QImage, int markerNumber=-1) -> int
        """
        return 0

    def markerDelete(self, p_int, int_markerNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerDelete(int, int markerNumber=-1) """
        pass

    def markerDeleteAll(self, int_markerNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerDeleteAll(int markerNumber=-1) """
        pass

    def markerDeleteHandle(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerDeleteHandle(int) """
        pass

    def markerFindNext(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerFindNext(int, int) -> int """
        return 0

    def markerFindPrevious(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerFindPrevious(int, int) -> int """
        return 0

    def markerLine(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.markerLine(int) -> int """
        return 0

    def markersAtLine(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.markersAtLine(int) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def modificationAttempted(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.modificationAttempted [signal] """
        pass

    def modificationChanged(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.modificationChanged[bool] [signal] """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveToMatchingBrace(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.moveToMatchingBrace() """
        pass

    def overwriteMode(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.overwriteMode() -> bool """
        return False

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def paper(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.paper() -> QColor """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.paste() """
        pass

    def positionFromLineIndex(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.positionFromLineIndex(int, int) -> int """
        return 0

    def read(self, QIODevice): # real signature unknown; restored from __doc__
        """ QsciScintilla.read(QIODevice) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def recolor(self, int_start=0, int_end=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.recolor(int start=0, int end=-1) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.redo() """
        pass

    def registerImage(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.registerImage(int, QPixmap)
        QsciScintilla.registerImage(int, QImage)
        """
        pass

    def removeSelectedText(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.removeSelectedText() """
        pass

    def replace(self, QString): # real signature unknown; restored from __doc__
        """ QsciScintilla.replace(QString) """
        pass

    def replaceSelectedText(self, QString): # real signature unknown; restored from __doc__
        """ QsciScintilla.replaceSelectedText(QString) """
        pass

    def resetFoldMarginColors(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetFoldMarginColors() """
        pass

    def resetHotspotBackgroundColor(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetHotspotBackgroundColor() """
        pass

    def resetHotspotForegroundColor(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetHotspotForegroundColor() """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resetMatchedBraceIndicator(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetMatchedBraceIndicator() """
        pass

    def resetSelectionBackgroundColor(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetSelectionBackgroundColor() """
        pass

    def resetSelectionForegroundColor(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetSelectionForegroundColor() """
        pass

    def resetUnmatchedBraceIndicator(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.resetUnmatchedBraceIndicator() """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def selectAll(self, bool_select=True): # real signature unknown; restored from __doc__
        """ QsciScintilla.selectAll(bool select=True) """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.selectedText() -> QString """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.selectionChanged [signal] """
        pass

    def selectionToEol(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.selectionToEol() -> bool """
        return False

    def selectToMatchingBrace(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.selectToMatchingBrace() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAnnotationDisplay(self, QsciScintilla_AnnotationDisplay): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAnnotationDisplay(QsciScintilla.AnnotationDisplay) """
        pass

    def setAutoCompletionCaseSensitivity(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionCaseSensitivity(bool) """
        pass

    def setAutoCompletionFillups(self, p_str): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionFillups(str) """
        pass

    def setAutoCompletionFillupsEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionFillupsEnabled(bool) """
        pass

    def setAutoCompletionReplaceWord(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionReplaceWord(bool) """
        pass

    def setAutoCompletionShowSingle(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionShowSingle(bool) """
        pass

    def setAutoCompletionSource(self, QsciScintilla_AutoCompletionSource): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionSource(QsciScintilla.AutoCompletionSource) """
        pass

    def setAutoCompletionThreshold(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionThreshold(int) """
        pass

    def setAutoCompletionUseSingle(self, QsciScintilla_AutoCompletionUseSingle): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionUseSingle(QsciScintilla.AutoCompletionUseSingle) """
        pass

    def setAutoCompletionWordSeparators(self, QStringList): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoCompletionWordSeparators(QStringList) """
        pass

    def setAutoIndent(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setAutoIndent(bool) """
        pass

    def setBackspaceUnindents(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setBackspaceUnindents(bool) """
        pass

    def setBraceMatching(self, QsciScintilla_BraceMatch): # real signature unknown; restored from __doc__
        """ QsciScintilla.setBraceMatching(QsciScintilla.BraceMatch) """
        pass

    def setCallTipsBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCallTipsBackgroundColor(QColor) """
        pass

    def setCallTipsForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCallTipsForegroundColor(QColor) """
        pass

    def setCallTipsHighlightColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCallTipsHighlightColor(QColor) """
        pass

    def setCallTipsPosition(self, QsciScintilla_CallTipsPosition): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCallTipsPosition(QsciScintilla.CallTipsPosition) """
        pass

    def setCallTipsStyle(self, QsciScintilla_CallTipsStyle): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCallTipsStyle(QsciScintilla.CallTipsStyle) """
        pass

    def setCallTipsVisible(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCallTipsVisible(int) """
        pass

    def setCaretForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCaretForegroundColor(QColor) """
        pass

    def setCaretLineBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCaretLineBackgroundColor(QColor) """
        pass

    def setCaretLineVisible(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCaretLineVisible(bool) """
        pass

    def setCaretWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCaretWidth(int) """
        pass

    def setColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setColor(QColor) """
        pass

    def setContractedFolds(self, list_of_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setContractedFolds(list-of-int) """
        pass

    def setCursorPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setCursorPosition(int, int) """
        pass

    def setDocument(self, QsciDocument): # real signature unknown; restored from __doc__
        """ QsciScintilla.setDocument(QsciDocument) """
        pass

    def setEdgeColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setEdgeColor(QColor) """
        pass

    def setEdgeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setEdgeColumn(int) """
        pass

    def setEdgeMode(self, QsciScintilla_EdgeMode): # real signature unknown; restored from __doc__
        """ QsciScintilla.setEdgeMode(QsciScintilla.EdgeMode) """
        pass

    def setEolMode(self, QsciScintilla_EolMode): # real signature unknown; restored from __doc__
        """ QsciScintilla.setEolMode(QsciScintilla.EolMode) """
        pass

    def setEolVisibility(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setEolVisibility(bool) """
        pass

    def setExtraAscent(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setExtraAscent(int) """
        pass

    def setExtraDescent(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setExtraDescent(int) """
        pass

    def setFirstVisibleLine(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setFirstVisibleLine(int) """
        pass

    def setFolding(self, QsciScintilla_FoldStyle, int_margin=2): # real signature unknown; restored from __doc__
        """ QsciScintilla.setFolding(QsciScintilla.FoldStyle, int margin=2) """
        pass

    def setFoldMarginColors(self, QColor, QColor_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setFoldMarginColors(QColor, QColor) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QsciScintilla.setFont(QFont) """
        pass

    def setHotspotBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setHotspotBackgroundColor(QColor) """
        pass

    def setHotspotForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setHotspotForegroundColor(QColor) """
        pass

    def setHotspotUnderline(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setHotspotUnderline(bool) """
        pass

    def setHotspotWrap(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setHotspotWrap(bool) """
        pass

    def setIndentation(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndentation(int, int) """
        pass

    def setIndentationGuides(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndentationGuides(bool) """
        pass

    def setIndentationGuidesBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndentationGuidesBackgroundColor(QColor) """
        pass

    def setIndentationGuidesForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndentationGuidesForegroundColor(QColor) """
        pass

    def setIndentationsUseTabs(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndentationsUseTabs(bool) """
        pass

    def setIndentationWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndentationWidth(int) """
        pass

    def setIndicatorDrawUnder(self, bool, int_indicatorNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndicatorDrawUnder(bool, int indicatorNumber=-1) """
        pass

    def setIndicatorForegroundColor(self, QColor, int_indicatorNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndicatorForegroundColor(QColor, int indicatorNumber=-1) """
        pass

    def setIndicatorOutlineColor(self, QColor, int_indicatorNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setIndicatorOutlineColor(QColor, int indicatorNumber=-1) """
        pass

    def setLexer(self, QsciLexer_lexer=None): # real signature unknown; restored from __doc__
        """ QsciScintilla.setLexer(QsciLexer lexer=None) """
        pass

    def setMarginLineNumbers(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginLineNumbers(int, bool) """
        pass

    def setMarginMarkerMask(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginMarkerMask(int, int) """
        pass

    def setMarginOptions(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginOptions(int) """
        pass

    def setMarginsBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginsBackgroundColor(QColor) """
        pass

    def setMarginSensitivity(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginSensitivity(int, bool) """
        pass

    def setMarginsFont(self, QFont): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginsFont(QFont) """
        pass

    def setMarginsForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginsForegroundColor(QColor) """
        pass

    def setMarginText(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.setMarginText(int, QString, int)
        QsciScintilla.setMarginText(int, QString, QsciStyle)
        QsciScintilla.setMarginText(int, QsciStyledText)
        QsciScintilla.setMarginText(int, list-of-QsciStyledText)
        """
        pass

    def setMarginType(self, p_int, QsciScintilla_MarginType): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarginType(int, QsciScintilla.MarginType) """
        pass

    def setMarginWidth(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.setMarginWidth(int, int)
        QsciScintilla.setMarginWidth(int, QString)
        """
        pass

    def setMarkerBackgroundColor(self, QColor, int_markerNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarkerBackgroundColor(QColor, int markerNumber=-1) """
        pass

    def setMarkerForegroundColor(self, QColor, int_markerNumber=-1): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMarkerForegroundColor(QColor, int markerNumber=-1) """
        pass

    def setMatchedBraceBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMatchedBraceBackgroundColor(QColor) """
        pass

    def setMatchedBraceForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMatchedBraceForegroundColor(QColor) """
        pass

    def setMatchedBraceIndicator(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setMatchedBraceIndicator(int) """
        pass

    def setModified(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setModified(bool) """
        pass

    def setOverwriteMode(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setOverwriteMode(bool) """
        pass

    def setPaper(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setPaper(QColor) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setReadOnly(bool) """
        pass

    def setSelection(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QsciScintilla.setSelection(int, int, int, int) """
        pass

    def setSelectionBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setSelectionBackgroundColor(QColor) """
        pass

    def setSelectionForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setSelectionForegroundColor(QColor) """
        pass

    def setSelectionToEol(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setSelectionToEol(bool) """
        pass

    def setTabIndents(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setTabIndents(bool) """
        pass

    def setTabWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setTabWidth(int) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QsciScintilla.setText(QString) """
        pass

    def setUnmatchedBraceBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setUnmatchedBraceBackgroundColor(QColor) """
        pass

    def setUnmatchedBraceForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setUnmatchedBraceForegroundColor(QColor) """
        pass

    def setUnmatchedBraceIndicator(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setUnmatchedBraceIndicator(int) """
        pass

    def setupViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setUtf8(self, bool): # real signature unknown; restored from __doc__
        """ QsciScintilla.setUtf8(bool) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWhitespaceBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWhitespaceBackgroundColor(QColor) """
        pass

    def setWhitespaceForegroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWhitespaceForegroundColor(QColor) """
        pass

    def setWhitespaceSize(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWhitespaceSize(int) """
        pass

    def setWhitespaceVisibility(self, QsciScintilla_WhitespaceVisibility): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWhitespaceVisibility(QsciScintilla.WhitespaceVisibility) """
        pass

    def setWrapIndentMode(self, QsciScintilla_WrapIndentMode): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWrapIndentMode(QsciScintilla.WrapIndentMode) """
        pass

    def setWrapMode(self, QsciScintilla_WrapMode): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWrapMode(QsciScintilla.WrapMode) """
        pass

    def setWrapVisualFlags(self, QsciScintilla_WrapVisualFlag, QsciScintilla_WrapVisualFlag_startFlag=None, int_indent=0): # real signature unknown; restored from __doc__
        """ QsciScintilla.setWrapVisualFlags(QsciScintilla.WrapVisualFlag, QsciScintilla.WrapVisualFlag startFlag=QsciScintilla.WrapFlagNone, int indent=0) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showUserList(self, p_int, QStringList): # real signature unknown; restored from __doc__
        """ QsciScintilla.showUserList(int, QStringList) """
        pass

    def standardCommands(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.standardCommands() -> QsciCommandSet """
        return QsciCommandSet

    def tabIndents(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.tabIndents() -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabWidth(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.tabWidth() -> int """
        return 0

    def text(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.text() -> QString
        QsciScintilla.text(int) -> QString
        """
        pass

    def textChanged(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.textChanged [signal] """
        pass

    def textHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.textHeight(int) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.undo() """
        pass

    def unindent(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.unindent(int) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def userListActivated(self, *args, **kwargs): # real signature unknown
        """ QsciScintilla.userListActivated[int, QString] [signal] """
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def whitespaceSize(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.whitespaceSize() -> int """
        return 0

    def whitespaceVisibility(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.whitespaceVisibility() -> QsciScintilla.WhitespaceVisibility """
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordAtLineIndex(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QsciScintilla.wordAtLineIndex(int, int) -> QString """
        pass

    def wordAtPoint(self, QPoint): # real signature unknown; restored from __doc__
        """ QsciScintilla.wordAtPoint(QPoint) -> QString """
        pass

    def wordCharacters(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.wordCharacters() -> str """
        return ""

    def wrapIndentMode(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.wrapIndentMode() -> QsciScintilla.WrapIndentMode """
        pass

    def wrapMode(self): # real signature unknown; restored from __doc__
        """ QsciScintilla.wrapMode() -> QsciScintilla.WrapMode """
        pass

    def write(self, QIODevice): # real signature unknown; restored from __doc__
        """ QsciScintilla.write(QIODevice) -> bool """
        return False

    def zoomIn(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.zoomIn(int)
        QsciScintilla.zoomIn()
        """
        pass

    def zoomOut(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QsciScintilla.zoomOut(int)
        QsciScintilla.zoomOut()
        """
        pass

    def zoomTo(self, p_int): # real signature unknown; restored from __doc__
        """ QsciScintilla.zoomTo(int) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    AcsAll = 1
    AcsAPIs = 3
    AcsDocument = 2
    AcsNone = 0
    AcusAlways = 2
    AcusExplicit = 1
    AcusNever = 0
    AiClosing = 4
    AiMaintain = 1
    AiOpening = 2
    AnnotationBoxed = 2
    AnnotationHidden = 0
    AnnotationStandard = 1
    Background = 22
    BottomLeftCorner = 10
    BoxedFoldStyle = 3
    BoxedMinus = 14
    BoxedMinusConnected = 15
    BoxedPlus = 12
    BoxedPlusConnected = 13
    BoxedTreeFoldStyle = 5
    BoxIndicator = 6
    CallTipsAboveText = 1
    CallTipsBelowText = 0
    CallTipsContext = 3
    CallTipsNoAutoCompletionContext = 2
    CallTipsNoContext = 1
    CallTipsNone = 0
    Circle = 0
    CircledFoldStyle = 2
    CircledMinus = 20
    CircledMinusConnected = 21
    CircledPlus = 18
    CircledPlusConnected = 19
    CircledTreeFoldStyle = 4
    DashesIndicator = 9
    DiagonalIndicator = 3
    DotBoxIndicator = 12
    DotsIndicator = 10
    DownTriangle = 6
    EdgeBackground = 2
    EdgeLine = 1
    EdgeNone = 0
    EolMac = 1
    EolUnix = 2
    EolWindows = 0
    FullRectangle = 26
    HiddenIndicator = 5
    Invisible = 5
    LeftRectangle = 27
    LeftSideRoundedSplitter = 17
    LeftSideSplitter = 11
    Minus = 7
    MoNone = 0
    MoSublineSelect = 1
    NoBraceMatch = 0
    NoFoldStyle = 0
    NumberMargin = 1
    PlainFoldStyle = 1
    PlainIndicator = 0
    Plus = 8
    Rectangle = 1
    RightArrow = 4
    RightTriangle = 2
    RoundBoxIndicator = 7
    RoundedBottomLeftCorner = 16
    SloppyBraceMatch = 2
    SmallRectangle = 3
    SquiggleIndicator = 1
    SquiggleLowIndicator = 11
    SquigglePixmapIndicator = 13
    StraightBoxIndicator = 8
    StrictBraceMatch = 1
    StrikeIndicator = 4
    SymbolMargin = 0
    SymbolMarginDefaultBackgroundColor = 2
    SymbolMarginDefaultForegroundColor = 3
    TextMargin = 4
    TextMarginRightJustified = 5
    ThreeDots = 23
    ThreeRightArrows = 24
    TTIndicator = 2
    Underline = 29
    VerticalLine = 9
    WrapCharacter = 2
    WrapFlagByBorder = 2
    WrapFlagByText = 1
    WrapFlagInMargin = 3
    WrapFlagNone = 0
    WrapIndentFixed = 0
    WrapIndentIndented = 2
    WrapIndentSame = 1
    WrapNone = 0
    WrapWord = 1
    WsInvisible = 0
    WsVisible = 1
    WsVisibleAfterIndent = 2


