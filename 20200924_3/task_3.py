a = input()
q = []
flag = 0
if a:
    while a:
        q.append(a)
        a = input()
for item in tuple(q):
    a = q.copy()
    a.remove(item)
    for item1 in a:
        if not set(item).isdisjoint(set(item1)):
            flag = 1
            break
    if not flag:
        print(item)
    flag = 0
