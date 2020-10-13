from fractions import Fraction as F


def suub(s, w, A, B):
    r1 = sum(c * s ** (len(A) - i - 1) for i, c in enumerate(A))
    r2 = sum(c * s ** (len(A) - i - 1) for i, c in enumerate(B))
    return r2 * w == r1


ALL = input().split(", ")

s, w, p1 = F(ALL[0]), F(ALL[1]), int(ALL[2])
p2 = int(ALL[4 + p1])

A = [F(c) for c in ALL[3:4 + p1]]
B = [F(c) for c in ALL[5 + p1:]]

print(suub(s, w, A, B))
