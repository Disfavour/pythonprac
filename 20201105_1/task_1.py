from re import *


print(bool(match(r"(\+|-)?(\d*)?(\.|\.\d+)?((e|E)([+-])?\d+)?$", input())))

