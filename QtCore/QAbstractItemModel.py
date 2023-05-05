# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
from typing import Dict, Type, List, overload
import sip as __sip

from .QObject import QObject

from .pyqtSignal import pyqtSignal
from .QModelIndex import QModelIndex
from .Qt import Qt
from .QMimeData import QMimeData
from .QStringList import QStringList
from .QVariant import QVariant
from .QDataStream import QDataStream
from .QSize import QSize

class QAbstractItemModel(QObject):
    """ QAbstractItemModel(QObject parent=None) """

    columnsAboutToBeInserted: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int)
    """ :type: pyqtSignal[QModelIndex parent, int start, int end]"""

    columnsAboutToBemoved: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    columnsInserted: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int)
    columnsMoved: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    columnsRemoved: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int)
    dataChanged: Type[pyqtSignal] = pyqtSignal(QModelIndex, QModelIndex)
    """ :type: pyqtSignal[QModelIndex topLeft, QModelIndex bottomRight]"""
    headerDataChanged: Type[pyqtSignal] = pyqtSignal(Qt.Orientation, int, int)
    layoutAboutToBeChanged: Type[pyqtSignal] = pyqtSignal()
    layoutChanged: Type[pyqtSignal] = pyqtSignal()
    modelAboutToBeReset: Type[pyqtSignal] = pyqtSignal()
    modelReset: Type[pyqtSignal] = pyqtSignal()
    rowsAboutToBeInserted: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int)
    rowsAboutToBeMoved: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    rowsInserted: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int)
    rowsMoved: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    rowsRemoved: Type[pyqtSignal] = pyqtSignal(QModelIndex, int, int)

    def beginInsertColumns(self, index: QModelIndex, row: int, col: int): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginInsertColumns(QModelIndex, int, int) """
        pass

    def beginInsertRows(self, index: QModelIndex, row: int, col: int): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginInsertRows(QModelIndex, int, int) """
        pass

    def beginMoveColumns(self, index: QModelIndex, row: int, col: int, index_1: QModelIndex, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginMoveColumns(QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginMoveRows(self, index: QModelIndex, row: int, col: int, index_1: QModelIndex, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginMoveRows(QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginRemoveColumns(self, index: QModelIndex, row: int, col: int): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginRemoveColumns(QModelIndex, int, int) """
        pass

    def beginRemoveRows(self, index: QModelIndex, row: int, col: int): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginRemoveRows(QModelIndex, int, int) """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginResetModel() """
        pass

    def buddy(self, index: QModelIndex)->QModelIndex: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.buddy(QModelIndex) -> QModelIndex """
        return QModelIndex

    def canFetchMore(self, index: QModelIndex)->bool: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.canFetchMore(QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, index: QModelIndex, index_1: QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.changePersistentIndex(QModelIndex, QModelIndex) """
        pass

    def changePersistentIndexList(self, indices: List[QModelIndex], indices_1: List[QModelIndex]): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.changePersistentIndexList(list-of-QModelIndex, list-of-QModelIndex) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, parent: QModelIndex=None, *args, **kwargs)->int: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, row: int, col: int, object_object=0)->QModelIndex: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.createIndex(int, int, object object=0) -> QModelIndex """
        return QModelIndex

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, index: QModelIndex, int_role=None)->QVariant: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        return QVariant

    def decodeData(self, row: int, col: int, index: QModelIndex, data_stream:QDataStream)->bool: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.decodeData(int, int, QModelIndex, QDataStream) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, data:QMimeData, Qt_DropAction, row: int, col: int, index: QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def encodeData(self, indices: List[QModelIndex], data_stream: QDataStream): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.encodeData(list-of-QModelIndex, QDataStream) """
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endInsertColumns() """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endInsertRows() """
        pass

    def endMoveColumns(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endMoveColumns() """
        pass

    def endMoveRows(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endMoveRows() """
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endRemoveColumns() """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endRemoveRows() """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endResetModel() """
        pass

    def fetchMore(self, index: QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.fetchMore(QModelIndex) """
        pass

    def flags(self, index: QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent: QModelIndex=None, *args, **kwargs)->bool: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def hasIndex(self, row: int, col: int, parent:QModelIndex=None, *args, **kwargs)->bool: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.hasIndex(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None)->QVariant: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        return QVariant

    def index(self, row: int, col: int, parent:QModelIndex=None, *args, **kwargs)->QModelIndex: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def insertColumn(self, p_int, parent:QModelIndex=None, *args, **kwargs)->bool: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertColumn(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertColumns(self, row: int, col: int, parent:QModelIndex=None, *args, **kwargs)->bool: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRow(self, p_int, parent:QModelIndex=None, *args, **kwargs)->bool: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertRow(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRows(self, row: int, col: int, parent:QModelIndex=None, *args, **kwargs)->bool: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def itemData(self, index: QModelIndex)->Dict[int, QVariant]: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.itemData(QModelIndex) -> dict-of-int-QVariant """
        pass

    def match(self, index: QModelIndex, p_int, variant: QVariant, int_hits=1, Qt_MatchFlags_flags=None, *args, **kwargs)->List[QModelIndex]: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.match(QModelIndex, int, QVariant, int hits=1, Qt.MatchFlags flags=Qt.MatchStartsWith|Qt.MatchWrap) -> list-of-QModelIndex """
        pass

    def mimeData(self, indices: List[QModelIndex])->QMimeData: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.mimeData(list-of-QModelIndex) -> QMimeData """
        return QMimeData

    def mimeTypes(self)->QStringList: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.mimeTypes() -> QStringList """
        return QStringList

    @overload
    def parent(self, index: QModelIndex)->QModelIndex:
        pass

    @overload
    def parent(self)->QObject:
        pass
    
    def parent(self, index: QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractItemModel.parent(QModelIndex) -> QModelIndex
        QAbstractItemModel.parent() -> QObject
        """
        return QModelIndex or QObject

    def persistentIndexList(self)->List[QModelIndex]: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.persistentIndexList() -> list-of-QModelIndex """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumn(self, p_int, parent:QModelIndex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeColumn(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeColumns(self, row: int, col: int, parent:QModelIndex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRow(self, p_int, parent:QModelIndex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeRow(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, row: int, col: int, parent:QModelIndex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.reset() """
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.resetInternalData() """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.revert() """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.roleNames() -> dict-of-int-QByteArray """
        pass

    def rowCount(self, parent: QModelIndex=None, *args, **kwargs)->int: # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, index: QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setItemData(self, index: QModelIndex, dict_of_int_QVariant): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setItemData(QModelIndex, dict-of-int-QVariant) -> bool """
        return False

    def setRoleNames(self, dict_of_int_QByteArray): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setRoleNames(dict-of-int-QByteArray) """
        pass

    def setSupportedDragActions(self, Qt_DropActions): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setSupportedDragActions(Qt.DropActions) """
        pass

    def sibling(self, row: int, col: int, index: QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.sibling(int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def span(self, index: QModelIndex)->QSize: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.span(QModelIndex) -> QSize """
        return QSize

    def submit(self)->bool: # real signature unknown; restored from __doc__
        """ QAbstractItemModel.submit() -> bool """
        return False

    def supportedDragActions(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.supportedDragActions() -> Qt.DropActions """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.supportedDropActions() -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


