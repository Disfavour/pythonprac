from types import FunctionType
from functools import wraps
import sys


def dumper(fun, name):
    @wraps(fun)
    def newf(self, *args, **kwargs):
        print(f"{name}: {args}, {kwargs}")
        return fun(self, *args, **kwargs)
    return newf

class dump(type):
    def __init__(self, name, parents, ns):
        #print("init", self, parents, ns)
        for attr, obj in vars(self).items():
            if isinstance(obj, FunctionType):
                setattr(self, attr, dumper(obj, attr))
        return super().__init__(name, parents, ns)

exec(sys.stdin.read())

