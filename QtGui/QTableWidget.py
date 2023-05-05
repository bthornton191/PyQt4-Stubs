# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
from typing import Type, overload


from .QTableView import QTableView
from .QTableWidgetItem import QTableWidgetItem
from ..QtCore.QPoint import QPoint
from ..QtCore.pyqtSignal import pyqtSignal
from .QWidget import QWidget

class QTableWidget(QTableView):
    """
    QTableWidget(QWidget parent=None)
    QTableWidget(int, int, QWidget parent=None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

        cellActivated: Type[pyqtSignal]
    # def cellActivated(self, *args, **kwargs): # real signature unknown
    #     """ QTableWidget.cellActivated[int, int] [signal] """
    #     pass

    cellChanged: Type[pyqtSignal]
    # def cellChanged(self, *args, **kwargs): # real signature unknown
    #     """ QTableWidget.cellChanged[int, int] [signal] """
    #     pass

    cellClicked: Type[pyqtSignal]
    # def cellClicked(self, *args, **kwargs): # real signature unknown
    #     """ QTableWidget.cellClicked[int, int] [signal] """
    #     pass

    cellDoubleClicked: Type[pyqtSignal]
    # def cellDoubleClicked(self, *args, **kwargs): # real signature unknown
    #     """ QTableWidget.cellDoubleClicked[int, int] [signal] """
    #     pass

    cellEntered: Type[pyqtSignal]
    # def cellEntered(self, *args, **kwargs): # real signature unknown
    #     """ QTableWidget.cellEntered[int, int] [signal] """
    #     pass

    cellPressed: Type[pyqtSignal]
    # def cellPressed(self, *args, **kwargs): # real signature unknown
    #     """ QTableWidget.cellPressed[int, int] [signal] """
    #     pass

    def cellWidget(self, row: int, col: int)->QWidget: # real signature unknown; restored from __doc__
        """ QTableWidget.cellWidget(int, int) -> QWidget """
        return QWidget

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QTableWidget.clear() """
        pass

    def clearContents(self): # real signature unknown; restored from __doc__
        """ QTableWidget.clearContents() """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closePersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.closePersistentEditor(QTableWidgetItem) """
        pass

    def column(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.column(QTableWidgetItem) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QTableWidget.columnCount() -> int """
        return 0

    def columnCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def columnMoved(self, *args, **kwargs): # real signature unknown
        pass

    def columnResized(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentCellChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.currentCellChanged[int, int, int, int] [signal] """
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ QTableWidget.currentColumn() -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ QTableWidget.currentItem() -> QTableWidgetItem """
        return QTableWidgetItem

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.currentItemChanged[QTableWidgetItem, QTableWidgetItem] [signal] """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ QTableWidget.currentRow() -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyRegionOffset(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QTableWidget.dropEvent(QDropEvent) """
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, p_int, p_int_1, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QTableWidget.dropMimeData(int, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.editItem(QTableWidgetItem) """
        pass

    def editorDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QTableWidget.event(QEvent) -> bool """
        return False

    def executeDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def findItems(self, QString, Qt_MatchFlags): # real signature unknown; restored from __doc__
        """ QTableWidget.findItems(QString, Qt.MatchFlags) -> list-of-QTableWidgetItem """
        pass

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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.horizontalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def horizontalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def indexFromItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.indexFromItem(QTableWidgetItem) -> QModelIndex """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.insertColumn(int) """
        pass

    def insertRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.insertRow(int) """
        pass

    def isIndexHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isItemSelected(self, item: QTableWidgetItem)->bool: # real signature unknown; restored from __doc__
        """ QTableWidget.isItemSelected(QTableWidgetItem) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ QTableWidget.isSortingEnabled() -> bool """
        return False

    def item(self, row: int, col: int)->QTableWidgetItem: # real signature unknown; restored from __doc__
        """ QTableWidget.item(int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemActivated(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemActivated[QTableWidgetItem] [signal] """
        pass

    @overload
    def itemAt(self, point: QPoint)->QTableWidgetItem:
        """QTableWidget.itemAt(QPoint) -> QTableWidgetItem
        """
        pass
    
    @overload
    def itemAt(self, row: int, col: int)->QTableWidgetItem:
        """QTableWidget.itemAt(int, int) -> QTableWidgetItem
        """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableWidget.itemAt(QPoint) -> QTableWidgetItem
        QTableWidget.itemAt(int, int) -> QTableWidgetItem
        """
        return QTableWidgetItem

    def itemChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemChanged[QTableWidgetItem] [signal] """
        pass

    def itemClicked(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemClicked[QTableWidgetItem] [signal] """
        pass

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemDoubleClicked[QTableWidgetItem] [signal] """
        pass

    def itemEntered(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemEntered[QTableWidgetItem] [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTableWidget.itemFromIndex(QModelIndex) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemPressed(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemPressed[QTableWidgetItem] [signal] """
        pass

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ QTableWidget.itemPrototype() -> QTableWidgetItem """
        return QTableWidgetItem

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ QTableWidget.items(QMimeData) -> list-of-QTableWidgetItem """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemSelectionChanged [signal] """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, list_of_QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.mimeData(list-of-QTableWidgetItem) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QTableWidget.mimeTypes() -> QStringList """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveCursor(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openPersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.openPersistentEditor(QTableWidgetItem) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeCellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableWidget.removeCellWidget(int, int) """
        pass

    def removeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.removeColumn(int) """
        pass

    def removeRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.removeRow(int) """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def row(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.row(QTableWidgetItem) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ QTableWidget.rowCount() -> int """
        return 0

    def rowCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def rowMoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowResized(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollToItem(self, QTableWidgetItem, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QTableWidget.scrollToItem(QTableWidgetItem, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ QTableWidget.selectedItems() -> list-of-QTableWidgetItem """
        pass

    def selectedRanges(self): # real signature unknown; restored from __doc__
        """ QTableWidget.selectedRanges() -> list-of-QTableWidgetSelectionRange """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCellWidget(self, p_int, p_int_1, QWidget): # real signature unknown; restored from __doc__
        """ QTableWidget.setCellWidget(int, int, QWidget) """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.setColumnCount(int) """
        pass

    def setCurrentCell(self, p_int, p_int_1, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableWidget.setCurrentCell(int, int)
        QTableWidget.setCurrentCell(int, int, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setCurrentItem(self, QTableWidgetItem, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableWidget.setCurrentItem(QTableWidgetItem)
        QTableWidget.setCurrentItem(QTableWidgetItem, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setHorizontalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setHorizontalHeaderItem(int, QTableWidgetItem) """
        pass

    def setHorizontalHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QTableWidget.setHorizontalHeaderLabels(QStringList) """
        pass

    def setHorizontalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def setItem(self, p_int, p_int_1, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setItem(int, int, QTableWidgetItem) """
        pass

    def setItemPrototype(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setItemPrototype(QTableWidgetItem) """
        pass

    def setItemSelected(self, QTableWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QTableWidget.setItemSelected(QTableWidgetItem, bool) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setRangeSelected(self, QTableWidgetSelectionRange, bool): # real signature unknown; restored from __doc__
        """ QTableWidget.setRangeSelected(QTableWidgetSelectionRange, bool) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.setRowCount(int) """
        pass

    def setSelection(self, *args, **kwargs): # real signature unknown
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTableWidget.setSortingEnabled(bool) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setupViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setVerticalHeaderItem(int, QTableWidgetItem) """
        pass

    def setVerticalHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QTableWidget.setVerticalHeaderLabels(QStringList) """
        pass

    def setVerticalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForRow(self, *args, **kwargs): # real signature unknown
        pass

    def sortItems(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QTableWidget.sortItems(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QTableWidget.supportedDropActions() -> Qt.DropActions """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def takeHorizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.takeHorizontalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeItem(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableWidget.takeItem(int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeVerticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.takeVerticalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.verticalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def verticalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def verticalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def viewOptions(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def visualColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.visualColumn(int) -> int """
        return 0

    def visualItemRect(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.visualItemRect(QTableWidgetItem) -> QRect """
        pass

    def visualRegionForSelection(self, *args, **kwargs): # real signature unknown
        pass

    def visualRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.visualRow(int) -> int """
        return 0

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


