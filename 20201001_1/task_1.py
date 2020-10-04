def F(a, b):
    t = type((1, 2))
    s = type([1, 2])
    ta = type(a)
    tb = type(b)
    if ta == tb and (ta == t or ta == s or ta == type("sdfs")):
        if ta == type("sdfs"):
            a = list(a)
            b = list(b)
        V = list(a)
        for i in a:
            for j in b:
                if i == j and j in V:
                    V.remove(j)
        if ta == type("sdfs"):
            return ''.join(V)
        return ta(V)
    else:
        return a - b


print(F(*eval(input())))
