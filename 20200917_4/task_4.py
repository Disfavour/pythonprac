a, n = eval(input())
x, y, z = 1, 1, 1
while x ** n + y ** n + z ** n <= a:
    while x ** n + y ** n + z ** n <= a:
        while x ** n + y ** n + z ** n <= a:
            if x ** n + y ** n + z ** n == a:
                break
            z += 1
        if x ** n + y ** n + z ** n == a:
            break
        z = 1
        y += 1
    if x ** n + y ** n + z ** n == a:
        break
    y = 1
    x += 1
if x ** n + y ** n + z ** n == a:
    print(x, y, z)
else:
    print("FAIL")

