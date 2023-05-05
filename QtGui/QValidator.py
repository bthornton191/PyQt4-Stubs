# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
from typing import Tuple
import PyQt4.QtCore as __PyQt4_QtCore

from ..QtCore.QObject import QObject

class QValidator(__PyQt4_QtCore.QObject):
    """ QValidator(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fixup(self, QString): # real signature unknown; restored from __doc__
        """ QValidator.fixup(QString) """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ QValidator.locale() -> QLocale """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ QValidator.setLocale(QLocale) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, s: str, pos: int)->Tuple[int, int]: # real signature unknown; restored from __doc__
        """ QValidator.validate(QString, int) -> (QValidator.State, int) """
        pass

    def __init__(self, parent: QObject=None): # real signature unknown; restored from __doc__
        pass

    Acceptable = 2
    Intermediate = 1
    Invalid = 0


