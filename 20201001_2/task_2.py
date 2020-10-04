def bin(item, spisok):
    if len(spisok) % 2 != 0:
        pos = (len(spisok) // 2)
    else:
        pos = (len(spisok) // 2) - 1
    if item == spisok[pos]:
        return True
    if len(spisok) <= 1:
        return False
    if item < spisok[pos]:
        return bin(item, spisok[:pos])
    else:
        return bin(item, spisok[pos + 1:])


a = eval(input())
a = list(a)
a[1] = list(a[1])
print(bin(*a))
