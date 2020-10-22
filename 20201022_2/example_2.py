def I(n):
    for i in range(n):
        yield i * 2 + 1

def II(k):
    for i in range(k):
        """for e in I(i):
            yield e"""
        yield from I(i)
