# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QValidator import QValidator

class QDoubleValidator(QValidator):
    """
    QDoubleValidator(QObject parent=None)
    QDoubleValidator(float, float, int, QObject parent=None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.bottom() -> float """
        return 0.0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def decimals(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.decimals() -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def notation(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.notation() -> QDoubleValidator.Notation """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBottom(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setBottom(float) """
        pass

    def setDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setDecimals(int) """
        pass

    def setNotation(self, QDoubleValidator_Notation): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setNotation(QDoubleValidator.Notation) """
        pass

    def setRange(self, p_float, p_float_1, int_decimals=0): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setRange(float, float, int decimals=0) """
        pass

    def setTop(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setTop(float) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.top() -> float """
        return 0.0

    def validate(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QDoubleValidator.validate(QString, int) -> (QValidator.State, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ScientificNotation = 1
    StandardNotation = 0


