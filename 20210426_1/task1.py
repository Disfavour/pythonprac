import math


def solveSquare(a, b, c):
    # a!= 0
    D = b * b - 4 * a * c
    if D > 0:
        return ((-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a))
    elif D == 0:
        return (-b / (2 * a), -b / (2 * a))
    # else:
    #     return Nonei
