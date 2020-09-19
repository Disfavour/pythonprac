a, b, c = eval(input())
v = [a, b, c]
v = sorted(v)
if v[-1] < v[1] + v[0] and v[0] > 0:
    print("triangle")
else:
    print("not triangle")
