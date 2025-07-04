

from CodingTools4.Functools.Decorator import initialize


@initialize()
class Test:
    """ Test class """
    def __init__(self, __test=None):
        print("init")
        self.name = "test"
        return
    def __call__(self, *args, **kwargs):
        print("call")
        return
    ...
Test: Test


def test(): return


if __name__ == '__main__':
    print(Test)
    print(Test.name)
    ...
