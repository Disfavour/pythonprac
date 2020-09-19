a = int(input())
if a % 25 == 0 and a % 2 == 0:
    print("A+", end = " ")
else:
    print("A-", end = " ")
if a % 25 == 0 and a % 2 != 0:
    print("B+", end = " ")
else:
    print("B-", end = " ")
if a % 8 == 0:
    print("C+")
else:
    print("C-")

