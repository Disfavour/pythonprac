import random
a = int(input())
b = []
for i in range(10):
    c = random.randint(1, 100)
    if c == a:
        continue
    b.append(c)
print(b)

