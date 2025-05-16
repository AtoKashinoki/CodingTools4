""" Error BasicStructure
This module provides a BasicStructure for the Error class.\n
このmoduleはErrorクラスのBasicStructureを提供します。
"""


""" Import """


from typing import Any

from time import time

from ..BasicStructure.Inheritance import Inheritance


"""
    Error basic structure class
"""


class Structure(Inheritance, Exception):
    """ Error structure """

    """ Initialize """

    def __init__(
            self,
            **kwargs: str
    ):
        """ Initialize message """
        self.__time__ = time()
        self.__message__ = self.__message__.format(**kwargs)
        Exception.__init__(self, self.__message__)
        return

    def __repr__(self) -> str:
        """ Return self class settings """
        kwargs_text = ", ".join(
            f"{key}={value.__repr__()}"
            for key, value in self.__kwargs__.items()
        )
        return f"{self.__class__.__name__}({kwargs_text})"

    """ message """
    __kwargs__: dict[str, Any]
    __message__: str
    @property
    def message(self) -> str: return self.__message__

    def __str__(self) -> str:
        """ Return message """
        return self.__message__

    """ time """
    __time__: float
    @property
    def time(self) -> float: return self.__time__

    def __eq__(self, other: Any) -> bool:
        """ Return self is equal to other """
        if isinstance(other, Structure):
            return self.__time__ == other.__time__

        elif isinstance(other, float):
            return self.__time__ == other

        return False

    def __ne__(self, other: Any) -> bool:
        """ Return self is not equal to other """
        if isinstance(other, Structure):
            return self.__time__ != other.__time__

        elif isinstance(other, float):
            return self.__time__ != other

        return False

    def __lt__(self, other: Any) -> bool:
        """ Return self is less than other """
        if isinstance(other, Structure):
            return self.__time__ < other.__time__

        elif isinstance(other, float):
            return self.__time__ < other

        return False

    def __le__(self, other: Any) -> bool:
        """ Return self is less than other """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: Any) -> bool:
        """ Return self is greater than other """
        if isinstance(other, Structure):
            return self.__time__ > other.__time__

        elif isinstance(other, float):
            return self.__time__ > other

        return False

    def __ge__(self, other: Any) -> bool:
        """ Return self is greater than or equal to other """
        return self.__gt__(other) or self.__eq__(other)

    ...


""" Initialize tools """


def create_structure(
        _error_type: type[Exception],
) -> type[Structure]:
    """ Create and return Error class """

    class NewStructure(Structure, _error_type):
        """ Error structure """

        def __init__(
                self,
                **kwargs: str
        ):
            """ Connect Structure.__init__ """
            Structure.__init__(self, **kwargs)
            return

        ...

    return NewStructure
