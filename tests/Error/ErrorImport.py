
from CodingTools4.Error.Import import PackageError


try:
    from . import BasicStructureA
    ...
except ImportError as e:
    BasicStructureA = PackageError(e)
    ...


if __name__ == '__main__':
    print(BasicStructureA)
    raise BasicStructureA
    ...
