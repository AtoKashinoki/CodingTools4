""" Functools.SpecialMethod


"""


""" Imports """


from typing import Any


"""
    Special methods
"""


def initialize(*args, **kwargs) -> Any:
    return lambda func: func(*args, **kwargs)


""" __repr__ method """


@initialize()
class __repr__:

    """ settings """

    settings_sep = ", "
    format_text = "{}({})"
    attr_e_message = "'{}' object has no attribute '__repr__'."

    """ process """
    def __call__(
            self,
            ins: Any,
            *args: Any,
            **kwargs: Any
    ) -> str | AttributeError:
        """ Return class settings that create from args """

        # argument setting text
        args_text = self.settings_sep.join(args)

        try:

            kw_settings = dict()
            for key, value in kwargs.items():

                if isinstance(value, type):
                    result = value.__name__
                    ...
                else:
                    result = value.__repr__()
                    ...

                if result[0] == "<" and result[-1] == ">":
                    raise AttributeError(self.attr_e_message.format(
                        value.__class__.__name__
                    ))
                kw_settings[key] = result
                continue

            kwargs_text = self.settings_sep.join(
                f"{key}={setting}"
                for key, setting in kw_settings.items()
            )
            ...

        except AttributeError as e:
            return e

        # return initialize text
        return self.format_text.format(
            ins.__class__.__name__,
            self.settings_sep.join([
                value
                for value in (args_text, kwargs_text)
                if len(value) > 0
            ]),
        )

    ...


__repr__: __repr__
