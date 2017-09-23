# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemView import QAbstractItemView

class QListView(QAbstractItemView):
    """ QListView(QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def batchSize(self): # real signature unknown; restored from __doc__
        """ QListView.batchSize() -> int """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearPropertyFlags(self): # real signature unknown; restored from __doc__
        """ QListView.clearPropertyFlags() """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QListView.currentChanged(QModelIndex, QModelIndex) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QListView.dataChanged(QModelIndex, QModelIndex) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyRegionOffset(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QListView.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QListView.dragMoveEvent(QDragMoveEvent) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QListView.dropEvent(QDropEvent) """
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editorDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QListView.event(QEvent) -> bool """
        return False

    def executeDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def flow(self): # real signature unknown; restored from __doc__
        """ QListView.flow() -> QListView.Flow """
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

    def gridSize(self): # real signature unknown; restored from __doc__
        """ QListView.gridSize() -> QSize """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ QListView.horizontalOffset() -> int """
        return 0

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QListView.indexAt(QPoint) -> QModelIndex """
        pass

    def indexesMoved(self, *args, **kwargs): # real signature unknown
        """ QListView.indexesMoved[list-of-QModelIndex] [signal] """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QListView.isIndexHidden(QModelIndex) -> bool """
        return False

    def isRowHidden(self, p_int): # real signature unknown; restored from __doc__
        """ QListView.isRowHidden(int) -> bool """
        return False

    def isSelectionRectVisible(self): # real signature unknown; restored from __doc__
        """ QListView.isSelectionRectVisible() -> bool """
        return False

    def isWrapping(self): # real signature unknown; restored from __doc__
        """ QListView.isWrapping() -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def layoutMode(self): # real signature unknown; restored from __doc__
        """ QListView.layoutMode() -> QListView.LayoutMode """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ QListView.modelColumn() -> int """
        return 0

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QListView.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QListView.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveCursor(self, QAbstractItemView_CursorAction, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QListView.moveCursor(QAbstractItemView.CursorAction, Qt.KeyboardModifiers) -> QModelIndex """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def movement(self): # real signature unknown; restored from __doc__
        """ QListView.movement() -> QListView.Movement """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QListView.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rectForIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QListView.rectForIndex(QModelIndex) -> QRect """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QListView.reset() """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QListView.resizeEvent(QResizeEvent) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ QListView.resizeMode() -> QListView.ResizeMode """
        pass

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QListView.rowsAboutToBeRemoved(QModelIndex, int, int) """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QListView.rowsInserted(QModelIndex, int, int) """
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QListView.scrollContentsBy(int, int) """
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QListView.scrollTo(QModelIndex, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ QListView.selectedIndexes() -> list-of-QModelIndex """
        pass

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ QListView.selectionChanged(QItemSelection, QItemSelection) """
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBatchSize(self, p_int): # real signature unknown; restored from __doc__
        """ QListView.setBatchSize(int) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setFlow(self, QListView_Flow): # real signature unknown; restored from __doc__
        """ QListView.setFlow(QListView.Flow) """
        pass

    def setGridSize(self, QSize): # real signature unknown; restored from __doc__
        """ QListView.setGridSize(QSize) """
        pass

    def setHorizontalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def setLayoutMode(self, QListView_LayoutMode): # real signature unknown; restored from __doc__
        """ QListView.setLayoutMode(QListView.LayoutMode) """
        pass

    def setModelColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QListView.setModelColumn(int) """
        pass

    def setMovement(self, QListView_Movement): # real signature unknown; restored from __doc__
        """ QListView.setMovement(QListView.Movement) """
        pass

    def setPositionForIndex(self, QPoint, QModelIndex): # real signature unknown; restored from __doc__
        """ QListView.setPositionForIndex(QPoint, QModelIndex) """
        pass

    def setResizeMode(self, QListView_ResizeMode): # real signature unknown; restored from __doc__
        """ QListView.setResizeMode(QListView.ResizeMode) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QListView.setRootIndex(QModelIndex) """
        pass

    def setRowHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QListView.setRowHidden(int, bool) """
        pass

    def setSelection(self, QRect, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QListView.setSelection(QRect, QItemSelectionModel.SelectionFlags) """
        pass

    def setSelectionRectVisible(self, bool): # real signature unknown; restored from __doc__
        """ QListView.setSelectionRectVisible(bool) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QListView.setSpacing(int) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformItemSizes(self, bool): # real signature unknown; restored from __doc__
        """ QListView.setUniformItemSizes(bool) """
        pass

    def setupViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def setViewMode(self, QListView_ViewMode): # real signature unknown; restored from __doc__
        """ QListView.setViewMode(QListView.ViewMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrap(self, bool): # real signature unknown; restored from __doc__
        """ QListView.setWordWrap(bool) """
        pass

    def setWrapping(self, bool): # real signature unknown; restored from __doc__
        """ QListView.setWrapping(bool) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ QListView.spacing() -> int """
        return 0

    def startDrag(self, Qt_DropActions): # real signature unknown; restored from __doc__
        """ QListView.startDrag(Qt.DropActions) """
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QListView.timerEvent(QTimerEvent) """
        pass

    def uniformItemSizes(self): # real signature unknown; restored from __doc__
        """ QListView.uniformItemSizes() -> bool """
        return False

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ QListView.updateGeometries() """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ QListView.verticalOffset() -> int """
        return 0

    def verticalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def verticalStepsPerItem(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QListView.viewMode() -> QListView.ViewMode """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ QListView.viewOptions() -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QListView.visualRect(QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QListView.visualRegionForSelection(QItemSelection) -> QRegion """
        return QRegion

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ QListView.wordWrap() -> bool """
        return False

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    Adjust = 1
    Batched = 1
    Fixed = 0
    Free = 1
    IconMode = 1
    LeftToRight = 0
    ListMode = 0
    SinglePass = 0
    Snap = 2
    Static = 0
    TopToBottom = 1


