from random import *

n = int(input())

g = list("аеёиоуыэюя".upper())
s = list("бвгджзйклмнпрстфхцчшщ".upper())

S = [[] for _ in range(3)]
S[0] += g
S[1] += [i + j for i in g for j in s]
S[2] += [j + i for i in g for j in s]
ans = ""
while len(ans) <= n - 1:
    ans += (choice(S[randrange(3)]))

print(ans)

