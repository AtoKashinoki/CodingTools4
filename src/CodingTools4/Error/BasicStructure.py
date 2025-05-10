""" Error BasicStructure
This module provides a BasicStructure for the Error class.\n
このモジュールはErrorクラスのBasicStructureを提供します。
"""


""" Execute block """


if __name__ == '__main__':
    raise RuntimeError(f"Cannot run '{__file__}'")


""" Import """


from abc import ABC


"""
    Error basic structure class
"""


class Structure(Exception, ABC):
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
                *_,
                **kwargs: str
        ):
            """ Connect Structure.__init__ """
            Structure.__init__(self, **kwargs)
            return

        ...

    return NewStructure
