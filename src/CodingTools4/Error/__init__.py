""" CodingTools4.Error
This package provides an error mechanism.\n
このpackageエラーに関する仕組みを提供します。
"""


"""
    Import tools
"""


try:
    from .BasicStructure import Structure
    ...
except ImportError as e:
    from .Import import PackageError
    Structure = PackageError(e)
    ...


try:
    from . import Import
    ...
except ImportError as e:
    from .Import import PackageError
    Import = PackageError(e)
    ...
