import sys

def deccount(f):
    __a = 0
    def newfun(*args, **kwargs):
        nonlocal __a
        __a += 1
        print(__a)
        return f(*args, **kwargs)
    return newfun


exec(sys.stdin.read())

