import Qt
from PyQt4.QtCore import pyqtSlot

from typing import Any
from typing import Callable
from typing import List
from typing import Union


class pyqtSignal(object):
    # TODO: Determine if pyqt accepts the parameters as any type of sequence other than a list, don't think it will.
    def __init__(self, types: List[type], name):
        """ Create one or more overloaded unbound signals as a class attribute.

            :param types: the types that define the C++ signature of the signal. Each type may be a Python type object or a string that is the name of a C++ type.
                Alternatively each may be a sequence of type arguments. In this case each sequence defines the signature of a different signal overload.
                The first overload will be the default.
            :param name: the name of the signal. If it is omitted then the name of the class attribute is used. This may only be given as a keyword argument.
            :return: an unbound signal
        """
        ...

    def connect(self, slot: Union[Callable, pyqtSlot, None], type: Qt.ConnectionType = Qt.AutoConnection, no_receiver_check: bool = False):
        """ Connect a signal to a slot. An exception will be raised if the connection failed.

        :param slot: the slot to connect to, either a Python callable or another bound signal.
        :param type: the type of the connection to make.
        :param no_receiver_check: suppress the check that the underlying C++ receiver instance still exists and deliver the signal anyway.
        :return: None
        """
        ...

    def disconnect(self, slot: Union[Callable, pyqtSignal, None] = None):
        """ Disconnect one or more slots from a signal. An exception will be raised if the slot is not connected to the signal or if the signal has no connections at all.

        :param slot: the optional slot to disconnect from, either a Python callable or another bound signal.
            If it is omitted then all slots connected to the signal are disconnected.
        :return: None.
        """
        ...

    def emit(self, *args: List[Any]):
        """ Emit a signal.

        :param args: the optional sequence of arguments to pass to any connected slots.
        :return: None
        """
        ...