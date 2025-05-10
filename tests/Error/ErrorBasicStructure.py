

from CodingTools4.Error.BasicStructure import Structure, create_structure


TypeError_ = create_structure(TypeError)


class Test(TypeError_):

    def __init__(self):
        super().__init__(
            self,
            test1 = "1", test2 = "2"
        )
        return

    __message__ = "test {test1} {test2}"
    ...


if __name__ == "__main__":
    print(Test.__bases__[0].__bases__)
    print(isinstance(Test(), TypeError))
    raise Test()
