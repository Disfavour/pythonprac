import math


def solveSquare(a, b, c):
    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        ans = min(x1, x2), max(x1, x2)
        return ans
    elif D == 0:
        x = -b / (2 * a)
        return x, x
