a = input().lower().split()
qwe = []
for item in a:
    last = ";"
    for i in item:
        if last.isalpha() and i.isalpha() and (last + i) not in qwe:
            qwe.append(last + i)
        last = i
print(len(qwe))

