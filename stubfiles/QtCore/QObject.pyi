from typing import List
from typing import Union
from typing import Type

from PyQt4 import QtCore


class QObject(object):
    destroyed = QtCore.pyqtSignal(QtCore.QObject)
    objectNameChanged = QtCore.pyqtSignal(QtCore.QString)

    staticMetaObject = ... # type: QtCore.QMetaObject
    """ This variable stores the meta-object for the class.

        A meta-object contains information about a class that inherits QObject, e.g. class name, superclass name, 
        properties, signals and slots. Every class that contains the Q_OBJECT macro will also have a meta-object.

        The meta-object information is required by the signal/slot connection mechanism and the property system. 
        The inherits() function also makes use of the meta-object.

        If you have a pointer to an object, you can use metaObject() to retrieve the 
        meta-object associated with that object.
    """

    # TODO: Determine if connect and disconnect should be included in this context (as opposed to solely pyqtSignal).
    # def connect(self,
    #             sender: QObject,
    #             signal: Union[str, QtCore.QString],
    #             method: Union[str, QtCore.QString],
    #             type_: QtCore.Qt.ConnectionType=QtCore.Qt.AutoConnection) -> QtCore.QMetaObject.Connection: ...
    # def disconnect(self,
    #                signal: Union[str, QtCore.QString]=None,
    #                receiver: QObject=None,
    #                method: Union[str, QtCore.QString]=None) -> bool: ...
    # TODO: Determine if startTimer and timerEvent are included in PyQt.
    # def startTimer(self):self, interval: int, timerType: QtCore.Qt.TimerType = QtCore.Qt.CoarseTimer) -> int:
    # def timerEvent(event: QtCore.QTimerEvent) -> None:

    def __init__(self, parent: QObject = ...) -> None: ...

    def blockSignals(self, block: bool) -> bool:
        """ If block is true, signals emitted by this object are blocked
            (i.e., emitting a signal will not invoke anything connected to it).
            If block is false, no such blocking will occur.

            The return value is the previous value of signalsBlocked().

            Note that the destroyed() signal will be emitted even if the signals for this object have been blocked.

            Signals emitted while being blocked are not buffered.
        """
        ...

    def children(self) -> List[QObject]:
        """ Returns a list of child objects.

            The first child added is the first object in the list and the last child added is the last object in the list,
            i.e. new children are appended at the end.

            Note that the list order changes when QWidget children are raised or lowered. A widget that is raised
            becomes the last object in the list, and a widget that is lowered becomes the first object in the list.
        """
        ...

    def dumpObjectInfo(self) -> None:
        """ Dumps information about signal connections, etc. for this object to the debug output.

            Note: before Qt 5.9, this function was not const.

            See also dumpObjectTree().
        """
        ...

    def dumpObjectTree(self) -> None:
        """Dumps a tree of children to the debug output.

            Note: before Qt 5.9, this function was not const.

            See also dumpObjectInfo().
        """

    def dynamicPropertyNames(self) -> List[QtCore.QByteArray]:
        """ Returns the names of all properties that were dynamically added to the object using setProperty().

            This function was introduced in Qt 4.2.
        """
        ...

    def event(self, e: QtCore.QEvent) -> bool:
        """ This virtual function receives events to an object and should return true
            if the event e was recognized and processed.

            The event() function can be reimplemented to customize the behavior of an object.

            Make sure you call the parent event class implementation for all the events you did not handle.
        """
        ...

    def eventFilter(self, watched: QObject, event: QtCore.QEvent) -> bool:
        """ Filters events if this object has been installed as an event filter for the watched object.

            In your reimplementation of this function, if you want to filter the event out,
            i.e. stop it being handled further, return true; otherwise return false.
        """
        ...

    def findChild(self, type_: Type, name: Union[str, QtCore.QString]) -> QObject:
        """ Returns the child of this object that can be cast into type T and that is called name,
            or 0 if there is no such object. Omitting the name argument causes all object names to be matched.
            The search is performed recursively, unless options specifies the option FindDirectChildrenOnly.

            If there is more than one child matching the search, the most direct ancestor is returned.
            If there are several direct ancestors, it is undefined which one will be returned.
            In that case, findChildren() should be used.

            This example returns a child QPushButton of parentWidget named "button1",
            even if the button isn't a direct child of the parent:
                QPushButton *button = parentWidget.findChild<QPushButton *>("button1");
        """
        ...

    def findChildren(self, types: List[Type], name: Union[str, QtCore.QString]) -> List[QObject]:
        """ Returns all children of this object with the given name that can be cast to type T,
            or an empty list if there are no such objects. Omitting the name argument causes all
            object names to be matched. The search is performed recursively, unless options specifies
            the option FindDirectChildrenOnly.

            The following example shows how to find a list of child QWidgets
            of the specified parentWidget named widget_name:
                QList<QWidget *> widgets = parentWidget.findChildren<QWidget *>("widget_name");
        """
        ...

    def inherits(self, className: Union[str, QtCore.QString]) -> bool:
        """ Returns true if this object is an instance of a class that inherits className or a
            QObject subclass that inherits className; otherwise returns false.

            A class is considered to inherit itself.
        """
        ...

    def installEventFilter(self, filterObject: QObject) -> None:
        """ Installs an event filter filterObj on this object. For example:
                monitoredObj->installEventFilter(filterObj);

            An event filter is an object that receives all events that are sent to this object.
            The filter can either stop the event or forward it to this object.
            The event filter filterObj receives events via its eventFilter() function.
            The eventFilter() function must return true if the event should be filtered, (i.e. stopped);
            otherwise it must return false.

            If multiple event filters are installed on a single object,
            the filter that was installed last is activated first.
        """
        ...

    def isWidgetType(self) -> bool:
        """ Returns true if the object is a widget; otherwise returns false.

            Calling this function is equivalent to calling inherits("QWidget"), except that it is much faster.
        """
        ...

    def isWindowType(self) -> bool:
        """ Returns true if the object is a window; otherwise returns false.

            Calling this function is equivalent to calling inherits("QWindow"), except that it is much faster.
        """
        ...

    def killTimer(self, id_: int) -> None:
        """ Kills the timer with timer identifier, id.

            The timer identifier is returned by startTimer() when a timer event is started.

            See also timerEvent() and startTimer().
        """
        ...

    def metaObject(self) -> QtCore.QMetaObject:
        """ Returns a pointer to the meta-object of this object.

            A meta-object contains information about a class that inherits QObject, e.g. class name, superclass name,
            properties, signals and slots. Every QObject subclass that contains the
            Q_OBJECT macro will have a meta-object.

            The meta-object information is required by the signal/slot connection mechanism and the property system.
            The inherits() function also makes use of the meta-object.

            If you have no pointer to an actual object instance but still want to access the meta-object of a class,
            you can use staticMetaObject.
        """
        ...

    def moveToThread(self, targetThread: QtCore.QThread) -> None:
        """ Changes the thread affinity for this object and its children. The object cannot be moved if it has a parent.
            Event processing will continue in the targetThread.

            To move an object to the main thread, use QApplication::instance() to retrieve a pointer
            to the current application, and then use QApplication::thread() to retrieve the thread in which
            the application lives. For example:
                myObject->moveToThread(QApplication::instance()->thread());

            If targetThread is zero, all event processing for this object and its children stops.

            Note that all active timers for the object will be reset. The timers are first stopped in the
            current thread and restarted (with the same interval) in the targetThread.
            As a result, constantly moving an object between threads can postpone timer events indefinitely.

            A QEvent::ThreadChange event is sent to this object just before the thread affinity is changed.
            You can handle this event to perform any special processing.
            Note that any new events that are posted to this object will be handled in the targetThread.

            Warning: This function is not thread-safe; the current thread must be same as the current thread affinity.
            In other words, this function can only "push" an object from the current thread to another thread,
            it cannot "pull" an object from any arbitrary thread to the current thread.

            See also thread().
        """
        ...

    def parent(self) -> QObject:
        """ Returns a pointer to the parent object.

            See also setParent() and children().
        """
        ...

    def property(self, name: Union[str, QtCore.QString]) -> QtCore.QVariant:
        """ Returns the value of the object's name property.

            If no such property exists, the returned variant is invalid.

            Information about all available properties is provided through the metaObject() and dynamicPropertyNames().

            See also setProperty(), QVariant::isValid(), metaObject(), and dynamicPropertyNames().
        """
        ...

    def removeEventFilter(self, obj: QObject) -> None:
        """ Removes an event filter object obj from this object. The request is ignored if such an event filter
            has not been installed.

            All event filters for this object are automatically removed when this object is destroyed.

            It is always safe to remove an event filter, even during event filter activation
            (i.e. from the eventFilter() function).

            See also installEventFilter(), eventFilter(), and event().
        """
        ...

    def sender(self) -> QObject:
        """ Returns a pointer to the object that sent the signal, if called in a slot activated by a signal;
            otherwise it returns 0. The pointer is valid only during the execution of the slot that calls this
            function from this object's thread context.

            The pointer returned by this function becomes invalid if the sender is destroyed,
            or if the slot is disconnected from the sender's signal.

            Warning: This function violates the object-oriented principle of modularity.
            However, getting access to the sender might be useful when many signals are connected to a single slot.

            Warning: As mentioned above, the return value of this function is not valid when the slot is called
            via a Qt::DirectConnection from a thread different from this object's thread.
            Do not use this function in this type of scenario.

            See also senderSignalIndex() and QSignalMapper.
        """
        ...

    def senderSignalIndex(self) -> int:
        """ Returns the meta-method index of the signal that called the currently executing slot,
            which is a member of the class returned by sender(). If called outside of a slot activated by a signal,
            -1 is returned.

            For signals with default parameters, this function will always return the index with all parameters,
            regardless of which was used with connect(). For example, the signal destroyed(QObject *obj = 0)
            will have two different indexes (with and without the parameter), but this function will always
            return the index with a parameter. This does not apply when overloading signals with different parameters.

            Warning: This function violates the object-oriented principle of modularity. However, getting access to
            the signal index might be useful when many signals are connected to a single slot.

            Warning: The return value of this function is not valid when the slot is called via a Qt::DirectConnection
            from a thread different from this object's thread. Do not use this function in this type of scenario.

            This function was introduced in Qt 4.8.

            See also sender(), QMetaObject::indexOfSignal(), and QMetaObject::method().
        """
        ...

    def setParent(self, parent: QObject) -> None:
        """ Makes the object a child of parent.

            See also parent() and children().
        """
        ...

    def setProperty(self, name: Union[str, QtCore.QString], value: Union[str, QtCore.QVariant]):
        """ Sets the value of the object's name property to value.

            If the property is defined in the class using Q_PROPERTY then true is
            returned on success and false otherwise. If the property is not defined using Q_PROPERTY,
            and therefore not listed in the meta-object, it is added as a dynamic property and false is returned.

            Information about all available properties is provided through the metaObject() and dynamicPropertyNames().

            Dynamic properties can be queried again using property() and can be removed by setting the property value
            to an invalid QVariant. Changing the value of a dynamic property causes a
            QDynamicPropertyChangeEvent to be sent to the object.

            Note: Dynamic properties starting with "_q_" are reserved for internal purposes.

            See also property(), metaObject(), dynamicPropertyNames(), and QMetaProperty::write().
        """
        ...

    def signalsBlocked(self) -> bool:
        """ Returns true if signals are blocked; otherwise returns false.

            Signals are not blocked by default.

            See also blockSignals() and QSignalBlocker.
        """
        ...

    def thread(self) -> QtCore.QThread:
        """ Returns the thread in which the object lives.

            See also moveToThread().
        """
        ...

    def tr(self,
           sourceText: Union[str, QtCore.QString],
           disambiguation: Union[str, QtCore.QString, None]=None,
           plurality: int=-1) -> Union[str, QtCore.QString]:
        """ Returns a translated version of sourceText, optionally based on a disambiguation string and value of n for
            strings containing plurals; otherwise returns QString::fromUtf8(sourceText)
            if no appropriate translated string is available.

            Example:
                void MainWindow::createActions()
                {
                    QMenu *fileMenu = menuBar()->addMenu(tr("&File"));
                    ...

            If the same sourceText is used in different roles within the same context,
            an additional identifying string may be passed in disambiguation (0 by default).
            In Qt 4.4 and earlier, this was the preferred way to pass comments to translators.

            Example:
                MyWindow::MyWindow()
                {
                    QLabel *senderLabel = new QLabel(tr("Name:"));
                    QLabel *recipientLabel = new QLabel(tr("Name:", "recipient"));
                    ...

            See Writing Source Code for Translation for a detailed description of Qt's
            translation mechanisms in general, and the Disambiguation section for information on disambiguation.

            Warning: This method is re-entrant only if all translators are installed before calling this method.
            Installing or removing translators while performing translations is not supported.
            Doing so will probably result in crashes or other undesirable behavior.

            See also QCoreApplication::translate() and Internationalization with Qt.
        """
        ...
