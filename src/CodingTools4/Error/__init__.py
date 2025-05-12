""" CodingTools4.Error
This module provides an error mechanism.\n
このモジュールはエラーに関する仕組みを提供します。
"""


"""
    Import tools
"""


try:
    from .BasicStructure import Structure
    ...
except ImportError as e:
    Structure = ImportError(e)
    ...
