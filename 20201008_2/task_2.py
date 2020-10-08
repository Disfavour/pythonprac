from fractions import Fraction as F
from decimal import Decimal as D


a = input().split(", ")
print(a)
s = a[0]
w = a[1]
A = a[2:2 + int(a[2]) + 2]
B = a[2 + int(a[2]) + 2:]
print(s, w, A, B)
s = F(s)
w = F(w)
A = list(enumerate(A))
B = reversed(list(enumerate(B)))
print(A, B)
