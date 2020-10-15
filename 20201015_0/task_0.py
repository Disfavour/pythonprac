W = input().split()

D = {}

for w in W:
    D[w] = D.get(w, 0) + 1

print(D)

