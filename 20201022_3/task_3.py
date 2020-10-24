from itertools import *


def f(i):
    for item in product('ORT', repeat=i):
        if "".join(item).count("TOR") == 2:
            yield "".join(item)


print(*list(f(int(input()))), sep=", ")

