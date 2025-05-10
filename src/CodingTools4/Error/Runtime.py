""" RuntimeError tools
This module provides a mechanism for RuntimeErrors.\n
このモジュールはRuntimeErrorに関する仕組みを提供します。
"""


""" Imports """


from .BasicStructure import create_structure


"""
    Runtime errors
"""


RuntimeError = create_structure(RuntimeError)


""" CannotRunError """


class CannotRunError(RuntimeError):
    """ Cannot run file error """

    """ Message """
    __message__ = "Cannot run '{target}' ."

    def __init__(self, _target: str):
        """ Initialize message """
        RuntimeError.__init__(
            self,
            target=_target
        )
        return

    ...


""" Execute block """


if __name__ == '__main__':
    raise CannotRunError(__file__)
