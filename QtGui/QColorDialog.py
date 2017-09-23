# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QColorDialog(QDialog):
    """
    QColorDialog(QWidget parent=None)
    QColorDialog(QColor, QWidget parent=None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QColorDialog.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def colorSelected(self, *args, **kwargs): # real signature unknown
        """ QColorDialog.colorSelected[QColor] [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentColor(self): # real signature unknown; restored from __doc__
        """ QColorDialog.currentColor() -> QColor """
        return QColor

    def currentColorChanged(self, *args, **kwargs): # real signature unknown
        """ QColorDialog.currentColorChanged[QColor] [signal] """
        pass

    def customColor(self, p_int): # real signature unknown; restored from __doc__
        """ QColorDialog.customColor(int) -> int """
        return 0

    def customCount(self): # real signature unknown; restored from __doc__
        """ QColorDialog.customCount() -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QColorDialog.done(int) """
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

    def getColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QColorDialog.getColor(QColor initial=Qt.white, QWidget parent=None) -> QColor
        QColorDialog.getColor(QColor, QWidget, QString, QColorDialog.ColorDialogOptions options=0) -> QColor
        """
        return QColor

    def getRgba(self, int_initial=2147483647, QWidget_parent=None): # real signature unknown; restored from __doc__
        """ QColorDialog.getRgba(int initial=2147483647, QWidget parent=None) -> (int, bool) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
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
        QColorDialog.open()
        QColorDialog.open(QObject, SLOT())
        QColorDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QColorDialog.options() -> QColorDialog.ColorDialogOptions """
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

    def selectedColor(self): # real signature unknown; restored from __doc__
        """ QColorDialog.selectedColor() -> QColor """
        return QColor

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentColor(self, QColor): # real signature unknown; restored from __doc__
        """ QColorDialog.setCurrentColor(QColor) """
        pass

    def setCustomColor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QColorDialog.setCustomColor(int, int) """
        pass

    def setOption(self, QColorDialog_ColorDialogOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QColorDialog.setOption(QColorDialog.ColorDialogOption, bool on=True) """
        pass

    def setOptions(self, QColorDialog_ColorDialogOptions): # real signature unknown; restored from __doc__
        """ QColorDialog.setOptions(QColorDialog.ColorDialogOptions) """
        pass

    def setStandardColor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QColorDialog.setStandardColor(int, int) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QColorDialog.setVisible(bool) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QColorDialog_ColorDialogOption): # real signature unknown; restored from __doc__
        """ QColorDialog.testOption(QColorDialog.ColorDialogOption) -> bool """
        return False

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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontUseNativeDialog = 4
    NoButtons = 2
    ShowAlphaChannel = 1


