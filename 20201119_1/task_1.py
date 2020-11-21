def deccount(f):
    __a = 0
    def newfun(*args):
        nonlocal __a
        __a += 1
        print(__a)
        return f(*args)
    return newfun


@deccount
def fun1(a, b):
    return a*2+b

@deccount
def fun2(x=1, y=2, z=3):
    return x+y+z

s = []
a = input()
while a:
    s.append(a)
    a = input()

s = "\n".join(s)
#print(s)
exec(s)

