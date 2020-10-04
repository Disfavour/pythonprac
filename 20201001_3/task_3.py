from math import *
def F(a, b, u):
    x = lambda x: eval(a)
    y = lambda x: eval(b)
    f = lambda x, y: eval(u)
    return lambda g: f(x(g), y(g))


a = eval(input())
K = F(*a)
print(K(eval(input())))
