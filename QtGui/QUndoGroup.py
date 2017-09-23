# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUndoGroup(__PyQt4_QtCore.QObject):
    """ QUndoGroup(QObject parent=None) """
    def activeStack(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.activeStack() -> QUndoStack """
        return QUndoStack

    def activeStackChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.activeStackChanged[QUndoStack] [signal] """
        pass

    def addStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoGroup.addStack(QUndoStack) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.canRedo() -> bool """
        return False

    def canRedoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.canRedoChanged[bool] [signal] """
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.canUndo() -> bool """
        return False

    def canUndoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.canUndoChanged[bool] [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.cleanChanged[bool] [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createRedoAction(self, QObject, QString_prefix=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QUndoGroup.createRedoAction(QObject, QString prefix=QString()) -> QAction """
        pass

    def createUndoAction(self, QObject, QString_prefix=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QUndoGroup.createUndoAction(QObject, QString prefix=QString()) -> QAction """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def indexChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.indexChanged[int] [signal] """
        pass

    def isClean(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.isClean() -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.redo() """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.redoText() -> QString """
        pass

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.redoTextChanged[QString] [signal] """
        pass

    def removeStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoGroup.removeStack(QUndoStack) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoGroup.setActiveStack(QUndoStack) """
        pass

    def stacks(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.stacks() -> list-of-QUndoStack """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.undo() """
        pass

    def undoText(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.undoText() -> QString """
        pass

    def undoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.undoTextChanged[QString] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


