# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QAbstractSlider(QWidget):
    """ QAbstractSlider(QWidget parent=None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def actionTriggered(self, *args, **kwargs): # real signature unknown
        """ QAbstractSlider.actionTriggered[int] [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractSlider.changeEvent(QEvent) """
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractSlider.event(QEvent) -> bool """
        return False

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

    def hasTracking(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.hasTracking() -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def invertedAppearance(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.invertedAppearance() -> bool """
        return False

    def invertedControls(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.invertedControls() -> bool """
        return False

    def isSliderDown(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.isSliderDown() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QAbstractSlider.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.maximum() -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimum(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.minimum() -> int """
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

    def orientation(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.orientation() -> Qt.Orientation """
        pass

    def pageStep(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.pageStep() -> int """
        return 0

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def rangeChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractSlider.rangeChanged[int, int] [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def repeatAction(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.repeatAction() -> QAbstractSlider.SliderAction """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInvertedAppearance(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setInvertedAppearance(bool) """
        pass

    def setInvertedControls(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setInvertedControls(bool) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setMaximum(int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setMinimum(int) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setOrientation(Qt.Orientation) """
        pass

    def setPageStep(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setPageStep(int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setRange(int, int) """
        pass

    def setRepeatAction(self, QAbstractSlider_SliderAction, int_thresholdTime=500, int_repeatTime=50): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setRepeatAction(QAbstractSlider.SliderAction, int thresholdTime=500, int repeatTime=50) """
        pass

    def setSingleStep(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setSingleStep(int) """
        pass

    def setSliderDown(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setSliderDown(bool) """
        pass

    def setSliderPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setSliderPosition(int) """
        pass

    def setTracking(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setTracking(bool) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSlider.setValue(int) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.singleStep() -> int """
        return 0

    def sliderChange(self, QAbstractSlider_SliderChange): # real signature unknown; restored from __doc__
        """ QAbstractSlider.sliderChange(QAbstractSlider.SliderChange) """
        pass

    def sliderMoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractSlider.sliderMoved[int] [signal] """
        pass

    def sliderPosition(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.sliderPosition() -> int """
        return 0

    def sliderPressed(self, *args, **kwargs): # real signature unknown
        """ QAbstractSlider.sliderPressed [signal] """
        pass

    def sliderReleased(self, *args, **kwargs): # real signature unknown
        """ QAbstractSlider.sliderReleased [signal] """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QAbstractSlider.timerEvent(QTimerEvent) """
        pass

    def triggerAction(self, QAbstractSlider_SliderAction): # real signature unknown; restored from __doc__
        """ QAbstractSlider.triggerAction(QAbstractSlider.SliderAction) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QAbstractSlider.value() -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractSlider.valueChanged[int] [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QAbstractSlider.wheelEvent(QWheelEvent) """
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    SliderMove = 7
    SliderNoAction = 0
    SliderOrientationChange = 1
    SliderPageStepAdd = 3
    SliderPageStepSub = 4
    SliderRangeChange = 0
    SliderSingleStepAdd = 1
    SliderSingleStepSub = 2
    SliderStepsChange = 2
    SliderToMaximum = 6
    SliderToMinimum = 5
    SliderValueChange = 3


