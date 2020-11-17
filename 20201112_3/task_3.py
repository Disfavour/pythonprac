while True:
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(input())
    except:
        print("Invalid input")
    else:
        a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        p = (a + b + c) / 2

        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

        if S == 0:
            print("Not a triangle")
            continue
        else:
            print(f'{S:.{2}f}')
        break

