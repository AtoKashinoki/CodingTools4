""" CodingTools4
This library provides several modules to facilitate Python development.\n
このlibraryはPythonによる開発を後押しする多くのモジュールを提供します。\

Homepage = https://github.com/AtoKashinoki/CodingTools4
"""


"""
    Import packages
"""


try:
    from . import Error
    ...
except ImportError as e:
    Error = ImportError(e)
    ...


try:
    from . import BasicStructure
    ...
except ImportError as e:
    BasicStructure = ImportError(e)
    ...
