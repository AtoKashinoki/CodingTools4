""" Functools.Decorator
This module provides a mechanism intended to assist the Decorator.
このmoduleはDecoratorの補助を目的とした仕組みを提供します。
"""


""" Imports """


from typing import Callable, Any, Type, TypeVar

from abc import abstractmethod

from functools import update_wrapper

from .SpecialMethod import __repr__
from ..BasicStructure.Inheritance import Inheritance


""" TypeVar """


T = TypeVar('T')


"""
    Decorator class systems
"""


""" Structure """


class Structure(Inheritance):
    """ Decorator class structure """

    """ Initializer """

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        return

    def __repr__(self):
        return str(__repr__(self, ))

    """ Call """
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        return

    ...


""" Generate decorator class """


# noinspection PyPep8Naming
def DecoratorClass(func: T) -> T:
    return func


@DecoratorClass
class DecoratorClass(Structure):
    """
        This decorator class wraps a callable object
        and generates a decorator class.
    """

    """ Initializer """

    def __init__(self, _callable: Callable[[Any], T]) -> None:
        """ Wraps decorator callable object """
        self.__callable: Callable[[Any], T] = _callable
        return

    """ Call """
    __callable: Callable[[Any], T]
    @property
    def decorator(self) -> Callable[[Any], T]: return self.__callable

    def __call__(self, *args, **kwargs) -> Callable[[Any], T]:
        try:
            result = self.__callable(*args, **kwargs)
        except TypeError as e:
            raise TypeError(e)
        return result

    ...


""" Generate factory class """


class FactoryClass(DecoratorClass):
    """
        This decorator class wraps a callable object
        and generates a factory class.
    """
    ...


"""
    Wrapper classes
"""


""" Initializer """


@FactoryClass
def initialize(*args, **kwargs) -> Callable[[Type[T]], T]:
    """ Initialize class function """

    @DecoratorClass
    def decorator(_cls: Type[T]) -> T:
        """ Initialize class function"""
        ins = _cls(*args, **kwargs)
        update_wrapper(ins, _cls, updated=())
        return ins

    return decorator
