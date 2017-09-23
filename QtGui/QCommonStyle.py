# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QStyle import QStyle

class QCommonStyle(QStyle):
    """ QCommonStyle() """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPainter, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.drawComplexControl(QStyle.ComplexControl, QStyleOptionComplex, QPainter, QWidget widget=None) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption, QPainter, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.drawControl(QStyle.ControlElement, QStyleOption, QPainter, QWidget widget=None) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption, QPainter, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.drawPrimitive(QStyle.PrimitiveElement, QStyleOption, QPainter, QWidget widget=None) """
        pass

    def generatedIconPixmap(self, QIcon_Mode, QPixmap, QStyleOption): # real signature unknown; restored from __doc__
        """ QCommonStyle.generatedIconPixmap(QIcon.Mode, QPixmap, QStyleOption) -> QPixmap """
        return QPixmap

    def hitTestComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPoint, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.hitTestComplexControl(QStyle.ComplexControl, QStyleOptionComplex, QPoint, QWidget widget=None) -> QStyle.SubControl """
        pass

    def layoutSpacingImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def pixelMetric(self, QStyle_PixelMetric, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.pixelMetric(QStyle.PixelMetric, QStyleOption option=None, QWidget widget=None) -> int """
        return 0

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCommonStyle.polish(QWidget)
        QCommonStyle.polish(QApplication)
        QCommonStyle.polish(QPalette) -> QPalette
        """
        return QPalette

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sizeFromContents(self, QStyle_ContentsType, QStyleOption, QSize, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.sizeFromContents(QStyle.ContentsType, QStyleOption, QSize, QWidget widget=None) -> QSize """
        pass

    def standardIconImplementation(self, QStyle_StandardPixmap, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.standardIconImplementation(QStyle.StandardPixmap, QStyleOption option=None, QWidget widget=None) -> QIcon """
        return QIcon

    def standardPixmap(self, QStyle_StandardPixmap, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.standardPixmap(QStyle.StandardPixmap, QStyleOption option=None, QWidget widget=None) -> QPixmap """
        return QPixmap

    def styleHint(self, QStyle_StyleHint, QStyleOption_option=None, QWidget_widget=None, QStyleHintReturn_returnData=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.styleHint(QStyle.StyleHint, QStyleOption option=None, QWidget widget=None, QStyleHintReturn returnData=None) -> int """
        return 0

    def subControlRect(self, QStyle_ComplexControl, QStyleOptionComplex, QStyle_SubControl, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.subControlRect(QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl, QWidget widget=None) -> QRect """
        pass

    def subElementRect(self, QStyle_SubElement, QStyleOption, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QCommonStyle.subElementRect(QStyle.SubElement, QStyleOption, QWidget widget=None) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCommonStyle.unpolish(QWidget)
        QCommonStyle.unpolish(QApplication)
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


