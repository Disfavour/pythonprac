from re import *


print(sub(r"([aeiouy])([^aeiouy]*)([aeiouy])", r"\3\2\1", input(), 1))

