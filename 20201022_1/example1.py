def ifun(n):
    yield 100500
    for i in range(n):
        yield i * 2 + 1
    yield 42

h = ifun(4)

#print(*ifun(4))

