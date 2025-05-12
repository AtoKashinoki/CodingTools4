""" CodingTools4.BasicStructure
This package provides a mechanism for managing classes based on inheritance.\n
このpackageは継承を前提としたクラスを管理する仕組みを提供します。
"""


""" Imports """


try:
    from .Inheritance import Inheritance
    ...
except ImportError as e:
    Inheritance = ImportError(e)
    ...
