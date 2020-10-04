def not_domination(a, b):
    return a[0] <= b[0] and a[1] <= b[1] and (a[0] < b[0] or a[1] < b[1])


def Pareto(*pairs):
    return tuple([a for a in pairs if all([(not not_domination(a, b)) for b in pairs])])


a = eval(input())
print(Pareto(*[i for i in a]))

