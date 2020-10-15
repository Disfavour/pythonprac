import sys
import random

A = int(sys.argv[1])
B = int(sys.argv[2])
C = int(sys.argv[3])
if len(sys.argv) > 4:
    S = int(sys.argv[4])
else:
    S = random.randrange(100500)
    print("Seed: ", S)
random.seed(S)
print(*(random.randint(A, B) for i in range(C)))

