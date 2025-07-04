

from CodingTools4.Functools.SpecialMethod import __repr__


class Test:

    def __init__(self, *args, **kwargs):
        self.repr = __repr__(self, *args, **kwargs)
        return

    repr: str
    def __repr__(self):
        return self.repr

    ...


if __name__ == "__main__":
    test = Test()
    print(test)
    print(repr(test))