def F(a, b):
    V = list(a)
    t = type((1, 2))
    s = type([1, 2])
    ta = type(a)
    tb = type(b)
    if ta == tb and ta == t or ta == s:
        for i in a:
            for j in b:
                if i == j:
                    V.remove(j)
        return ta(V)
    elif ta == tb:
        return ta(a - b)
    else:
        return("CANT")
print(F(eval(input()), eval(input())))
