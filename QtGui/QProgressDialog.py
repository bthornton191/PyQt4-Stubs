# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QProgressDialog(QDialog):
    """
    QProgressDialog(QWidget parent=None, Qt.WindowFlags flags=0)
    QProgressDialog(QString, QString, int, int, QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def autoClose(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.autoClose() -> bool """
        return False

    def autoReset(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.autoReset() -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.cancel() """
        pass

    def canceled(self, *args, **kwargs): # real signature unknown
        """ QProgressDialog.canceled [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.closeEvent(QCloseEvent) """
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
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

    def forceShow(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.forceShow() """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.labelText() -> QString """
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.maximum() -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimum(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.minimum() -> int """
        return 0

    def minimumDuration(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.minimumDuration() -> int """
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

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QProgressDialog.open()
        QProgressDialog.open(QObject, SLOT())
        QProgressDialog.open(callable)
        """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.reset() """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.resizeEvent(QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoClose(self, bool): # real signature unknown; restored from __doc__
        """ QProgressDialog.setAutoClose(bool) """
        pass

    def setAutoReset(self, bool): # real signature unknown; restored from __doc__
        """ QProgressDialog.setAutoReset(bool) """
        pass

    def setBar(self, QProgressBar): # real signature unknown; restored from __doc__
        """ QProgressDialog.setBar(QProgressBar) """
        pass

    def setCancelButton(self, QPushButton): # real signature unknown; restored from __doc__
        """ QProgressDialog.setCancelButton(QPushButton) """
        pass

    def setCancelButtonText(self, QString): # real signature unknown; restored from __doc__
        """ QProgressDialog.setCancelButtonText(QString) """
        pass

    def setLabel(self, QLabel): # real signature unknown; restored from __doc__
        """ QProgressDialog.setLabel(QLabel) """
        pass

    def setLabelText(self, QString): # real signature unknown; restored from __doc__
        """ QProgressDialog.setLabelText(QString) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setMaximum(int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setMinimum(int) """
        pass

    def setMinimumDuration(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setMinimumDuration(int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QProgressDialog.setRange(int, int) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setValue(int) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.value() -> int """
        return 0

    def wasCanceled(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.wasCanceled() -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


