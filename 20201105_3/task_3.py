from re import *


print(sub(r"(?<=0)([1-9]{2,4})(?=0)(.*?)(?<=0)([1-9]{2,4})(?=0)", r"\3\2\1", input(), 1))

