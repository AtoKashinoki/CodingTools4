""" Error BasicStructure
This module provides a BasicStructure for the Error class.\n
このモジュールはErrorクラスのBasicStructureを提供します。
"""


""" Import """


from ..BasicStructure.Inheritance import Inheritance


"""
    Error basic structure class
"""


class Structure(Inheritance, Exception):
    """ Error structure """

    def __init__(
            self,
            *_,
            **kwargs: str
    ):
        """ Initialize message """
        self.__message__ = self.__message__.format(**kwargs)
        Exception.__init__(self, self.__message__)
        return

    """ message """
    __message__: str
    @property
    def message(self) -> str: return self.__message__

    ...


""" Initialize tools """


def create_structure(
        _error_type: type[Exception],
) -> type[Structure]:
    """ Create and return Error class """

    class NewStructure(_error_type, Structure):
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
