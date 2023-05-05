from __future__ import annotations
# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
from PyQt4.QtCore import QObject
import sip as __sip
from .QMetaEnum import QMetaEnum
from .QMetaMethod import QMetaMethod
from .QVariant import QVariant


class QMetaProperty(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QMetaProperty()
    QMetaProperty(QMetaProperty)
    """
    def enumerator(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.enumerator() -> QMetaEnum """
        return QMetaEnum

    def hasNotifySignal(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.hasNotifySignal() -> bool """
        return False

    def hasStdCppSet(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.hasStdCppSet() -> bool """
        return False

    def isConstant(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isConstant() -> bool """
        return False

    def isDesignable(self, obj: QObject=None)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isDesignable(QObject object=None) -> bool """
        return False

    def isEditable(self, obj: QObject=None)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isEditable(QObject object=None) -> bool """
        return False

    def isEnumType(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isEnumType() -> bool """
        return False

    def isFinal(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isFinal() -> bool """
        return False

    def isFlagType(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isFlagType() -> bool """
        return False

    def isReadable(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isReadable() -> bool """
        return False

    def isResettable(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isResettable() -> bool """
        return False

    def isScriptable(self, obj: QObject=None)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isScriptable(QObject object=None) -> bool """
        return False

    def isStored(self, obj: QObject=None)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isStored(QObject object=None) -> bool """
        return False

    def isUser(self, obj: QObject=None)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isUser(QObject object=None) -> bool """
        return False

    def isValid(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isValid() -> bool """
        return False

    def isWritable(self)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.isWritable() -> bool """
        return False

    def name(self)->str: # real signature unknown; restored from __doc__
        """ QMetaProperty.name() -> str """
        return ""

    def notifySignal(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.notifySignal() -> QMetaMethod """
        return QMetaMethod

    def notifySignalIndex(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.notifySignalIndex() -> int """
        return 0

    def propertyIndex(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.propertyIndex() -> int """
        return 0

    def read(self, obj: QObject)->QVariant: # real signature unknown; restored from __doc__
        """ QMetaProperty.read(QObject) -> QVariant """
        return QVariant

    def reset(self, obj: QObject)->bool: # real signature unknown; restored from __doc__
        """ QMetaProperty.reset(QObject) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.type() -> Type """
        pass

    def typeName(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.typeName() -> str """
        return ""

    def userType(self): # real signature unknown; restored from __doc__
        """ QMetaProperty.userType() -> int """
        return 0

    def write(self, obj:QObject, qvariant: QVariant): # real signature unknown; restored from __doc__
        """ QMetaProperty.write(QObject, QVariant) -> bool """
        return False

    def __init__(self, prop: QMetaProperty=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



