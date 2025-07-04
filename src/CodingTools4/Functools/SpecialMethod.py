""" Functools.SpecialMethod
This module provides a mechanism for the purpose of assisting special methods.
このmoduleは特殊メソッドの補助を目的とした仕組みを提供します。
"""


""" Imports """


from typing import Any

from .Decorator import initialize


"""
    Special methods
"""


""" __repr__ method """


@initialize()
class __repr__:
    """ __repr__ special method object """

    """ settings """

    __settings_sep = ", "
    __format_text = "{}({})"
    __attr_e_message = "'{}' object has no attribute '__repr__'."

    """ process """
    def __call__(
            self,
            ins: Any,
            *args: Any,
            **kwargs: Any
    ) -> str | AttributeError:
        """ Return class settings that create from args """

        # argument setting text
        args_text = self.__settings_sep.join(args)

        kw_settings = dict()
        for key, value in kwargs.items():

            if isinstance(value, type):
                result = value.__name__
                ...
            else:
                result = value.__repr__()
                ...

            if result[0] == "<" and result[-1] == ">":
                raise AttributeError(self.__attr_e_message.format(
                    value.__class__.__name__
                ))
            kw_settings[key] = result
            continue

        kwargs_text = self.__settings_sep.join(
            f"{key}={setting}"
            for key, setting in kw_settings.items()
        )
        ...

        # return initialize text
        return self.__format_text.format(
            ins.__class__.__name__,
            self.__settings_sep.join([
                value
                for value in (args_text, kwargs_text)
                if len(value) > 0
            ]),
        )

    ...
