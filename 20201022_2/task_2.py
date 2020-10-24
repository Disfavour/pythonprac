from itertools import islice, filterfalse, tee


def even(seq):
    return filterfalse(lambda x: x%2, seq)


"""def slide(a):
    for i in range(len(a) - 2):
        yield from even(a[i: i + 3])"""


def slide(seq):
    seq = iter(seq)
    while True:
        s, seq = tee(seq, 2)
        win = list(islice(s, 3))
        if len(win) < 3:
            return
        yield from even(win)
        next(seq)


print(*list(slide(list(eval(input())))), sep=", ")

