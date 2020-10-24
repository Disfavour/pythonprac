from itertools import *


print(list(filter(lambda x: "".join(x).count("TOR") == 2, product('ORT', repeat=int(input())))))

