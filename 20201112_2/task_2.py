from collections import *


class nestr(UserString):
    def __neg__(self):
        self.data = ("".join(reversed(list(self.data))))
        return self.__class__(self.data)


a = nestr("aabbcdefg")
b = nestr("abbbklopafdsdg")
print(eval(input()))

