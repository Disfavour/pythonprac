def Pareto(*pairs):
    return tuple(a for a in pairs if all(not domination(a, b) for b in pairs))

def domination(a, b):
    return b[0] >= a[0] and b[1] >= a[1] and (b[0] > a[0] or b[1] > a[1])
print(Pareto(eval(input())))

