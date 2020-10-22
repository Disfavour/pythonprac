from itertools import *

def fib(m, n):
    last = [1]
    last1 = 1
    for i in count():
        last.append(i + last1)
        if m <=  len(last) <= n:
            yield last[-1]
        last1 = i
