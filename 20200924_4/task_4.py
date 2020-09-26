string = input()
#string = "A12B2425C543A21B4"
a = ["A", "B", "C"]
b = ["1", "2", "3", "4", "5"]
flag = 0
for index, item in enumerate(string):
    if flag:
        if item in a:
            print(index_old, item_old)
            flag -= 1
        elif index == len(string) - 1 and item in b:
            print(index, item)
    if item == a[1]:
        flag += 1
    index_old = index
    item_old = item
