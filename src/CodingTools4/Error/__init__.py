""" CodingTools4.Error
This module provides an error mechanism.\n
このモジュールはエラーに関する仕組みを提供します。
"""


""" Execute block """


if __name__ == '__main__':
    from .Runtime import CannotRunError
    raise CannotRunError(__file__)


"""
    Import
"""
