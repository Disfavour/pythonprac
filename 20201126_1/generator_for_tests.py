import sys


data = [i.encode() for i in ["3baabca", "3baabcaf", "3baabc"]]

with open("data/1.in", "wb") as f:
    f.write(data[0])

with open("data/2.in", "wb") as f:
    f.write(data[1])

with open("data/3.in", "wb") as f:
    f.write(data[2])

