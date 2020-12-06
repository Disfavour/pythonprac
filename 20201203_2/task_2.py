import sys


def chan(self):
    for a, t in self.__annotations__.items():
        if not hasattr(self, a) or not isinstance(getattr(self, a), t):
            return False
    return True


class check(type):
    def __init__(self, name, parents, ns):
        super().__init__(name, parents, ns)
        self.check_annotations = chan


exec(sys.stdin.read())

