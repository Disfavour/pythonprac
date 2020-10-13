from numpy import *
from decimal import Decimal as D


def f(a):
    return lambda x: eval(a)


c = input()
d = eval(input())

x, y = d[:2], d[2:]
g = f(c)

ax, ay = 80, 25

dx = x[1] - x[0]
dy = y[1] - y[0]

dx = dx / (ax - 1)
dy = dy / (ay - 1)

art = [" " * ax for __ in range(ay)]

j = x[0]
kj = 0

while j <= x[1] + dx * 0.7:
    i = y[0]
    i1 = g(j)
    ki = 0
    while i <= y[1] + dy * 0.7:
        if i >= i1:
            art[ki] = art[ki][:kj] + "*" + art[ki][kj + 1:]
            break
        last = g(j)
        i += dy
        ki += 1
    j += dx
    kj += 1

art.reverse()

for item in art:
    print(item)
