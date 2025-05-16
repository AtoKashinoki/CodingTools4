""" Error.Import
This module provides an ErrorClass for ImportError.
このmoduleはImportErrorに関するErrorClassを提供します。
"""


""" Imports """


from .BasicStructure import create_structure


"""
    Import errors
"""


ImportError = create_structure(ImportError)


""" PackageError """


class PackageError(ImportError):
    """ ImportError for package """

    """ message """
    __message__: str = None

    def __init__(self, _error: Exception) -> None:
        self.__kwargs__ = {"_error": _error}
        self.__message__ = str(_error)
        ImportError.__init__(self)
        return
    ...
