import sys
from random import *
import urllib.request

N = int(sys.argv[1])

if len(sys.argv) > 2:
    S = int(sys.argv[2])
    seed(S)

D = dict()
data = urllib.request.urlopen("https://uneex.org/LecturesCMC/PythonIntro2020/06_DictCollection?action=AttachFile&do"
                                                  "=get&target=anna.txt").read().decode().lower()

D = dict()
last = None

for i in data:
    if last is not None and last.isalpha() and i.isalpha():
        if last + i in D:
            D[last + i] += 1
        else:
            D[last + i] = 1
    last = i

password = choices(list(D.keys()), weights=list(D.values()), k=1)[0]

while len(password) < N:
    tmp = dict()
    for word, number in D.items():
        if word[0] == password[len(password) - 1]:
            tmp[word] = number
    password += choices(list(tmp.keys()), weights=list(tmp.values()), k=1)[0][1]

print(password)

