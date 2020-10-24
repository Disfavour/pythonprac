def fib(m, n):
    k = [1, 1]
    i = m
    while m <= i <= n:
        if i == 1 or i == 2:
            yield 1
            i += 1
            continue
        yield sum(k)
        k.reverse()
        k[1] = sum(k)
        i += 1


print(*list(fib(*eval(input()))), sep=", ")

