# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip

from QObject import QObject


class QAbstractItemModel(QObject):
    """ QAbstractItemModel(QObject parent=None) """

    columnsAboutToBeInserted = pyqtSignal(QModelIndex, int, int)
    """ :type: pyqtSignal[QModelIndex parent, int start, int end]"""

    columnsAboutToBemoved = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    columnsInserted = pyqtSignal(QModelIndex, int, int)
    columnsMoved = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    columnsRemoved = pyqtSignal(QModelIndex, int, int)
    dataChanged = pyqtSignal(QModelIndex, QModelIndex)
    """ :type: pyqtSignal[QModelIndex topLeft, QModelIndex bottomRight]"""
    headerDataChanged = pyqtSignal(Qt.Orientation, int, int)
    layoutAboutToBeChanged = pyqtSignal()
    layoutChanged = pyqtSignal()
    modelAboutToBeReset = pyqtSignal()
    modelReset = pyqtSignal()
    rowsAboutToBeInserted = pyqtSignal(QModelIndex, int, int)
    rowsAboutToBeMoved = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    rowsInserted = pyqtSignal(QModelIndex, int, int)
    rowsMoved = pyqtSignal(QModelIndex, int, int, QModelIndex, int)
    rowsRemoved = pyqtSignal(QModelIndex, int, int)

    def beginInsertColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginInsertColumns(QModelIndex, int, int) """
        pass

    def beginInsertRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginInsertRows(QModelIndex, int, int) """
        pass

    def beginMoveColumns(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginMoveColumns(QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginMoveRows(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginMoveRows(QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginRemoveColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginRemoveColumns(QModelIndex, int, int) """
        pass

    def beginRemoveRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginRemoveRows(QModelIndex, int, int) """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginResetModel() """
        pass

    def buddy(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.buddy(QModelIndex) -> QModelIndex """
        return QModelIndex

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.canFetchMore(QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.changePersistentIndex(QModelIndex, QModelIndex) """
        pass

    def changePersistentIndexList(self, list_of_QModelIndex, list_of_QModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.changePersistentIndexList(list-of-QModelIndex, list-of-QModelIndex) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, p_int, p_int_1, object_object=0): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.createIndex(int, int, object object=0) -> QModelIndex """
        return QModelIndex

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        return QVariant

    def decodeData(self, p_int, p_int_1, QModelIndex, QDataStream): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.decodeData(int, int, QModelIndex, QDataStream) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def encodeData(self, list_of_QModelIndex, QDataStream): # real signature unknown; restored from __doc__
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

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.fetchMore(QModelIndex) """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def hasIndex(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.hasIndex(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        return QVariant

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def insertColumn(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertColumn(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRow(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertRow(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.itemData(QModelIndex) -> dict-of-int-QVariant """
        pass

    def match(self, QModelIndex, p_int, QVariant, int_hits=1, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.match(QModelIndex, int, QVariant, int hits=1, Qt.MatchFlags flags=Qt.MatchStartsWith|Qt.MatchWrap) -> list-of-QModelIndex """
        pass

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.mimeData(list-of-QModelIndex) -> QMimeData """
        return QMimeData

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.mimeTypes() -> QStringList """
        return QStringList

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractItemModel.parent(QModelIndex) -> QModelIndex
        QAbstractItemModel.parent() -> QObject
        """
        return QModelIndex or QObject

    def persistentIndexList(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.persistentIndexList() -> list-of-QModelIndex """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumn(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeColumn(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRow(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.removeRow(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
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

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """ QAbstractItemModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setItemData(self, QModelIndex, dict_of_int_QVariant): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setItemData(QModelIndex, dict-of-int-QVariant) -> bool """
        return False

    def setRoleNames(self, dict_of_int_QByteArray): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setRoleNames(dict-of-int-QByteArray) """
        pass

    def setSupportedDragActions(self, Qt_DropActions): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setSupportedDragActions(Qt.DropActions) """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.sibling(int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.span(QModelIndex) -> QSize """
        return QSize

    def submit(self): # real signature unknown; restored from __doc__
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


