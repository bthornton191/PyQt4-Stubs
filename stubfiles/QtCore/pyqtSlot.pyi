from typing import AnyStr
from typing import List
from typing import Union
from typing import Optional


def pyqtSlot(*types: Union[AnyStr, List[type]], name: Optional[AnyStr] = None, result: Optional[Union[AnyStr, type]] = None):
    """ Although PyQt4 allows any Python callable to be used as a slot when connecting signals,
        it is sometimes necessary to explicitly mark a Python method as being a Qt slot and to provide a
        C++ signature for it. PyQt4 provides the pyqtSlot() function decorator to do this.

    :param name: the types that define the C++ signature of the slot. Each type may be a Python type object or a string that is the name of a C++ type.
    :param result: the name of the slot that will be seen by C++.
        If omitted the name of the Python method being decorated will be used. This may only be given as a keyword argument.
    :param types: the type of the result and may be a Python type object or a string that specifies a C++ type. This may only be given as a keyword argument.
    :return: None
    """
    ...
