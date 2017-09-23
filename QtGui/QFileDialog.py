# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QFileDialog(QDialog):
    """
    QFileDialog(QWidget, Qt.WindowFlags)
    QFileDialog(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString())
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ QFileDialog.accept() """
        pass

    def acceptMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.acceptMode() -> QFileDialog.AcceptMode """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QFileDialog.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def confirmOverwrite(self): # real signature unknown; restored from __doc__
        """ QFileDialog.confirmOverwrite() -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.currentChanged[QString] [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSuffix(self): # real signature unknown; restored from __doc__
        """ QFileDialog.defaultSuffix() -> QString """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def directory(self): # real signature unknown; restored from __doc__
        """ QFileDialog.directory() -> QDir """
        pass

    def directoryEntered(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.directoryEntered[QString] [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QFileDialog.done(int) """
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def fileMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.fileMode() -> QFileDialog.FileMode """
        pass

    def fileSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.fileSelected[QString] [signal] """
        pass

    def filesSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.filesSelected[QStringList] [signal] """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.filter() -> QDir.Filters """
        pass

    def filters(self): # real signature unknown; restored from __doc__
        """ QFileDialog.filters() -> QStringList """
        pass

    def filterSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.filterSelected[QString] [signal] """
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

    def getExistingDirectory(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getExistingDirectory(QWidget parent=None, QString caption=QString(), QString directory=QString(), QFileDialog.Options options=QFileDialog.ShowDirsOnly) -> QString """
        pass

    def getOpenFileName(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileName(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString selectedFilter=None, QFileDialog.Options options=0) -> QString """
        pass

    def getOpenFileNameAndFilter(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileNameAndFilter(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString initialFilter=QString(), QFileDialog.Options options=0) -> (QString, QString) """
        pass

    def getOpenFileNames(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileNames(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString selectedFilter=None, QFileDialog.Options options=0) -> QStringList """
        pass

    def getOpenFileNamesAndFilter(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileNamesAndFilter(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString initialFilter=QString(), QFileDialog.Options options=0) -> (QString, QString) """
        pass

    def getSaveFileName(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getSaveFileName(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString selectedFilter=None, QFileDialog.Options options=0) -> QString """
        pass

    def getSaveFileNameAndFilter(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getSaveFileNameAndFilter(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString initialFilter=QString(), QFileDialog.Options options=0) -> (QString, QString) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ QFileDialog.history() -> QStringList """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ QFileDialog.iconProvider() -> QFileIconProvider """
        return QFileIconProvider

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isNameFilterDetailsVisible(self): # real signature unknown; restored from __doc__
        """ QFileDialog.isNameFilterDetailsVisible() -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QFileDialog.isReadOnly() -> bool """
        return False

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ QFileDialog.itemDelegate() -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self, QFileDialog_DialogLabel): # real signature unknown; restored from __doc__
        """ QFileDialog.labelText(QFileDialog.DialogLabel) -> QString """
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QFileDialog.nameFilters() -> QStringList """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.open()
        QFileDialog.open(QObject, SLOT())
        QFileDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QFileDialog.options() -> QFileDialog.Options """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def proxyModel(self): # real signature unknown; restored from __doc__
        """ QFileDialog.proxyModel() -> QAbstractProxyModel """
        return QAbstractProxyModel

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ QFileDialog.resolveSymlinks() -> bool """
        return False

    def restoreState(self, QByteArray): # real signature unknown; restored from __doc__
        """ QFileDialog.restoreState(QByteArray) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ QFileDialog.saveState() -> QByteArray """
        pass

    def selectedFiles(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedFiles() -> QStringList """
        pass

    def selectedFilter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedFilter() -> QString """
        pass

    def selectedNameFilter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedNameFilter() -> QString """
        pass

    def selectFile(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.selectFile(QString) """
        pass

    def selectFilter(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.selectFilter(QString) """
        pass

    def selectNameFilter(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.selectNameFilter(QString) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptMode(self, QFileDialog_AcceptMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setAcceptMode(QFileDialog.AcceptMode) """
        pass

    def setConfirmOverwrite(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setConfirmOverwrite(bool) """
        pass

    def setDefaultSuffix(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.setDefaultSuffix(QString) """
        pass

    def setDirectory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.setDirectory(QString)
        QFileDialog.setDirectory(QDir)
        """
        pass

    def setFileMode(self, QFileDialog_FileMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setFileMode(QFileDialog.FileMode) """
        pass

    def setFilter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.setFilter(QString)
        QFileDialog.setFilter(QDir.Filters)
        """
        pass

    def setFilters(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileDialog.setFilters(QStringList) """
        pass

    def setHistory(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileDialog.setHistory(QStringList) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ QFileDialog.setIconProvider(QFileIconProvider) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QFileDialog.setItemDelegate(QAbstractItemDelegate) """
        pass

    def setLabelText(self, QFileDialog_DialogLabel, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.setLabelText(QFileDialog.DialogLabel, QString) """
        pass

    def setNameFilter(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilter(QString) """
        pass

    def setNameFilterDetailsVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilterDetailsVisible(bool) """
        pass

    def setNameFilters(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilters(QStringList) """
        pass

    def setOption(self, QFileDialog_Option, bool_on=True): # real signature unknown; restored from __doc__
        """ QFileDialog.setOption(QFileDialog.Option, bool on=True) """
        pass

    def setOptions(self, QFileDialog_Options): # real signature unknown; restored from __doc__
        """ QFileDialog.setOptions(QFileDialog.Options) """
        pass

    def setProxyModel(self, QAbstractProxyModel): # real signature unknown; restored from __doc__
        """ QFileDialog.setProxyModel(QAbstractProxyModel) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setReadOnly(bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setResolveSymlinks(bool) """
        pass

    def setSidebarUrls(self, list_of_QUrl): # real signature unknown; restored from __doc__
        """ QFileDialog.setSidebarUrls(list-of-QUrl) """
        pass

    def setViewMode(self, QFileDialog_ViewMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setViewMode(QFileDialog.ViewMode) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setVisible(bool) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sidebarUrls(self): # real signature unknown; restored from __doc__
        """ QFileDialog.sidebarUrls() -> list-of-QUrl """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QFileDialog_Option): # real signature unknown; restored from __doc__
        """ QFileDialog.testOption(QFileDialog.Option) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.viewMode() -> QFileDialog.ViewMode """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Accept = 3
    AcceptOpen = 0
    AcceptSave = 1
    AnyFile = 0
    Detail = 0
    Directory = 2
    DirectoryOnly = 4
    DontConfirmOverwrite = 4
    DontResolveSymlinks = 2
    DontUseCustomDirectoryIcons = 128
    DontUseNativeDialog = 16
    DontUseSheet = 8
    ExistingFile = 1
    ExistingFiles = 3
    FileName = 1
    FileType = 2
    HideNameFilterDetails = 64
    List = 1
    LookIn = 0
    ReadOnly = 32
    Reject = 4
    ShowDirsOnly = 1


