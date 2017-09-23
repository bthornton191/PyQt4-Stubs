# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QTextFrame import QTextFrame

class QTextTable(QTextFrame):
    """ QTextTable(QTextDocument) """
    def appendColumns(self, p_int): # real signature unknown; restored from __doc__
        """ QTextTable.appendColumns(int) """
        pass

    def appendRows(self, p_int): # real signature unknown; restored from __doc__
        """ QTextTable.appendRows(int) """
        pass

    def cellAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextTable.cellAt(int, int) -> QTextTableCell
        QTextTable.cellAt(int) -> QTextTableCell
        QTextTable.cellAt(QTextCursor) -> QTextTableCell
        """
        return QTextTableCell

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columns(self): # real signature unknown; restored from __doc__
        """ QTextTable.columns() -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QTextTable.format() -> QTextTableFormat """
        return QTextTableFormat

    def insertColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextTable.insertColumns(int, int) """
        pass

    def insertRows(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextTable.insertRows(int, int) """
        pass

    def mergeCells(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextTable.mergeCells(int, int, int, int)
        QTextTable.mergeCells(QTextCursor)
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextTable.removeColumns(int, int) """
        pass

    def removeRows(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextTable.removeRows(int, int) """
        pass

    def resize(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextTable.resize(int, int) """
        pass

    def rowEnd(self, QTextCursor): # real signature unknown; restored from __doc__
        """ QTextTable.rowEnd(QTextCursor) -> QTextCursor """
        return QTextCursor

    def rows(self): # real signature unknown; restored from __doc__
        """ QTextTable.rows() -> int """
        return 0

    def rowStart(self, QTextCursor): # real signature unknown; restored from __doc__
        """ QTextTable.rowStart(QTextCursor) -> QTextCursor """
        return QTextCursor

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, QTextTableFormat): # real signature unknown; restored from __doc__
        """ QTextTable.setFormat(QTextTableFormat) """
        pass

    def splitCell(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QTextTable.splitCell(int, int, int, int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QTextDocument): # real signature unknown; restored from __doc__
        pass


