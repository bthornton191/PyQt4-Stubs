# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QInputDialog(QDialog):
    """ QInputDialog(QWidget parent=None, Qt.WindowFlags flags=0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cancelButtonText(self): # real signature unknown; restored from __doc__
        """ QInputDialog.cancelButtonText() -> QString """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def comboBoxItems(self): # real signature unknown; restored from __doc__
        """ QInputDialog.comboBoxItems() -> QStringList """
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

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.done(int) """
        pass

    def doubleDecimals(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleDecimals() -> int """
        return 0

    def doubleMaximum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleMaximum() -> float """
        return 0.0

    def doubleMinimum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleMinimum() -> float """
        return 0.0

    def doubleValue(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleValue() -> float """
        return 0.0

    def doubleValueChanged(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.doubleValueChanged[float] [signal] """
        pass

    def doubleValueSelected(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.doubleValueSelected[float] [signal] """
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

    def getDouble(self, QWidget, QString, QString_1, float_value=0, float_min=-2147483647, float_max=2147483647, int_decimals=1, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QInputDialog.getDouble(QWidget, QString, QString, float value=0, float min=-2147483647, float max=2147483647, int decimals=1, Qt.WindowFlags flags=0) -> (float, bool) """
        pass

    def getInt(self, QWidget, QString, QString_1, int_value=0, int_min=-2147483647, int_max=2147483647, int_step=1, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QInputDialog.getInt(QWidget, QString, QString, int value=0, int min=-2147483647, int max=2147483647, int step=1, Qt.WindowFlags flags=0) -> (int, bool) """
        pass

    def getInteger(self, QWidget, QString, QString_1, int_value=0, int_min=-2147483647, int_max=2147483647, int_step=1, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QInputDialog.getInteger(QWidget, QString, QString, int value=0, int min=-2147483647, int max=2147483647, int step=1, Qt.WindowFlags flags=0) -> (int, bool) """
        pass

    def getItem(self, QWidget, QString, QString_1, QStringList, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QInputDialog.getItem(QWidget, QString, QString, QStringList, int current=0, bool editable=True, Qt.WindowFlags flags=0) -> (QString, bool)
        QInputDialog.getItem(QWidget, QString, QString, QStringList, int, bool, Qt.WindowFlags, Qt.InputMethodHints) -> (QString, bool)
        """
        pass

    def getText(self, QWidget, QString, QString_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QInputDialog.getText(QWidget, QString, QString, QLineEdit.EchoMode mode=QLineEdit.Normal, QString text=QString(), Qt.WindowFlags flags=0) -> (QString, bool)
        QInputDialog.getText(QWidget, QString, QString, QLineEdit.EchoMode, QString, Qt.WindowFlags, Qt.InputMethodHints) -> (QString, bool)
        """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMode(self): # real signature unknown; restored from __doc__
        """ QInputDialog.inputMode() -> QInputDialog.InputMode """
        pass

    def intMaximum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intMaximum() -> int """
        return 0

    def intMinimum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intMinimum() -> int """
        return 0

    def intStep(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intStep() -> int """
        return 0

    def intValue(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intValue() -> int """
        return 0

    def intValueChanged(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.intValueChanged[int] [signal] """
        pass

    def intValueSelected(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.intValueSelected[int] [signal] """
        pass

    def isComboBoxEditable(self): # real signature unknown; restored from __doc__
        """ QInputDialog.isComboBoxEditable() -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ QInputDialog.labelText() -> QString """
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QInputDialog.minimumSizeHint() -> QSize """
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

    def okButtonText(self): # real signature unknown; restored from __doc__
        """ QInputDialog.okButtonText() -> QString """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QInputDialog.open()
        QInputDialog.open(QObject, SLOT())
        QInputDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QInputDialog.options() -> QInputDialog.InputDialogOptions """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
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

    def setCancelButtonText(self, QString): # real signature unknown; restored from __doc__
        """ QInputDialog.setCancelButtonText(QString) """
        pass

    def setComboBoxEditable(self, bool): # real signature unknown; restored from __doc__
        """ QInputDialog.setComboBoxEditable(bool) """
        pass

    def setComboBoxItems(self, QStringList): # real signature unknown; restored from __doc__
        """ QInputDialog.setComboBoxItems(QStringList) """
        pass

    def setDoubleDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleDecimals(int) """
        pass

    def setDoubleMaximum(self, p_float): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleMaximum(float) """
        pass

    def setDoubleMinimum(self, p_float): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleMinimum(float) """
        pass

    def setDoubleRange(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleRange(float, float) """
        pass

    def setDoubleValue(self, p_float): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleValue(float) """
        pass

    def setInputMode(self, QInputDialog_InputMode): # real signature unknown; restored from __doc__
        """ QInputDialog.setInputMode(QInputDialog.InputMode) """
        pass

    def setIntMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntMaximum(int) """
        pass

    def setIntMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntMinimum(int) """
        pass

    def setIntRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntRange(int, int) """
        pass

    def setIntStep(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntStep(int) """
        pass

    def setIntValue(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntValue(int) """
        pass

    def setLabelText(self, QString): # real signature unknown; restored from __doc__
        """ QInputDialog.setLabelText(QString) """
        pass

    def setOkButtonText(self, QString): # real signature unknown; restored from __doc__
        """ QInputDialog.setOkButtonText(QString) """
        pass

    def setOption(self, QInputDialog_InputDialogOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QInputDialog.setOption(QInputDialog.InputDialogOption, bool on=True) """
        pass

    def setOptions(self, QInputDialog_InputDialogOptions): # real signature unknown; restored from __doc__
        """ QInputDialog.setOptions(QInputDialog.InputDialogOptions) """
        pass

    def setTextEchoMode(self, QLineEdit_EchoMode): # real signature unknown; restored from __doc__
        """ QInputDialog.setTextEchoMode(QLineEdit.EchoMode) """
        pass

    def setTextValue(self, QString): # real signature unknown; restored from __doc__
        """ QInputDialog.setTextValue(QString) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QInputDialog.setVisible(bool) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QInputDialog.sizeHint() -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QInputDialog_InputDialogOption): # real signature unknown; restored from __doc__
        """ QInputDialog.testOption(QInputDialog.InputDialogOption) -> bool """
        return False

    def textEchoMode(self): # real signature unknown; restored from __doc__
        """ QInputDialog.textEchoMode() -> QLineEdit.EchoMode """
        pass

    def textValue(self): # real signature unknown; restored from __doc__
        """ QInputDialog.textValue() -> QString """
        pass

    def textValueChanged(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.textValueChanged[QString] [signal] """
        pass

    def textValueSelected(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.textValueSelected[QString] [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    DoubleInput = 2
    IntInput = 1
    NoButtons = 1
    TextInput = 0
    UseListViewForComboBoxItems = 2


