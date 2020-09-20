i = 3
while i < 7:
    print("\t", i, end="")
    i += 1
print()
i = 3
while i < 7:
    j = 3
    print(i, end="\t")
    while j < 7:
        s = i * j
        if s % 10 + s // 10 != 6:
            print(i * j, end="\t")
        else:
            print(":=)", end="\t")
        j += 1
    print()
    i += 1

