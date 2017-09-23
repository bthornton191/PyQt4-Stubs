# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QAbstractPrintDialog(QDialog):
    """ QAbstractPrintDialog(QPrinter, QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addEnabledOption(self, QAbstractPrintDialog_PrintDialogOption): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.addEnabledOption(QAbstractPrintDialog.PrintDialogOption) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enabledOptions(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.enabledOptions() -> QAbstractPrintDialog.PrintDialogOptions """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.exec_() -> int """
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

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def fromPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.fromPage() -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isOptionEnabled(self, QAbstractPrintDialog_PrintDialogOption): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.isOptionEnabled(QAbstractPrintDialog.PrintDialogOption) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maxPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.maxPage() -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.minPage() -> int """
        return 0

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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.printer() -> QPrinter """
        return QPrinter

    def printRange(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.printRange() -> QAbstractPrintDialog.PrintRange """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabledOptions(self, QAbstractPrintDialog_PrintDialogOptions): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setEnabledOptions(QAbstractPrintDialog.PrintDialogOptions) """
        pass

    def setFromTo(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setFromTo(int, int) """
        pass

    def setMinMax(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setMinMax(int, int) """
        pass

    def setOptionTabs(self, list_of_QWidget): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setOptionTabs(list-of-QWidget) """
        pass

    def setPrintRange(self, QAbstractPrintDialog_PrintRange): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setPrintRange(QAbstractPrintDialog.PrintRange) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.toPage() -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QPrinter, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    AllPages = 0
    CurrentPage = 3
    None = 0
    None_ = 0
    PageRange = 2
    PrintCollateCopies = 16
    PrintCurrentPage = 64
    PrintPageRange = 4
    PrintSelection = 2
    PrintShowPageSize = 8
    PrintToFile = 1
    Selection = 1


