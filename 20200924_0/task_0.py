for i in range(3, 7):
    print("\t", i, end="")
print()
for i in range(3, 7):
    print(i, end="\t")
    for j in range(3, 7):
        s = i * j
        if s % 10 + s // 10 != 6:
            print(i * j, end="\t")
        else:
            print(":=)", end="\t")
    print()

