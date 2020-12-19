import sys

class Num:
    def __get__(self, obj, cls):
        try:
            return obj._value
        except AttributeError:
            obj._value = 0
            return obj._value

    def __set__(self, obj, val):
        if hasattr(val, "real"):
            obj._value = val
        elif hasattr(val, "__len__"):
            obj._value = len(val)
        else:
            obj._value = 0

    def __delete__(self, obj):
        obj._value = None

exec(sys.stdin.read())
