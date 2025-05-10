""" Error BasicStructure
"""


""" Execute block """


if __name__ == '__main__':
    raise RuntimeError('cannot run this script')


""" Import """


from abc import ABC


"""
    Error basic structure class
"""


class Structure(Exception, ABC):
    """ Error basic structure """

    def __init__(
            self,
            message: str = ""
    ):
        """ Initialize message """
        self.__message = message
        Exception.__init__(self, message)
        return

    """ message """
    __message: str
    @property
    def message(self) -> str: return self.__message

    ...

