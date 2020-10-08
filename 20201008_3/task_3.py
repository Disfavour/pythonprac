a, b = input().split()
# qwe asdaffs

#   qwe
# asdas

L = max(len(a), len(b))
fmt = "{:>" + f"{L}" + "}"
print(fmt)
print(fmt.format(a))
print(fmt.format(b))



