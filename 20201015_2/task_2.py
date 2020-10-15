from random import *

n = int(input())

g = list("аеёиоуыэюя".upper())
s = list("бвгджзйклмнпрстфхцчшщ".upper())

q = g + [k + l for k in g for l in s] + [k + l for k in s for l in g]
S = []
while len(S) <= n - 1:
    S.append(sample(g, 1))
print(*S)

