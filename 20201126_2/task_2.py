import sys


text = sys.stdin.read()
print(text.encode('latin1', errors='replace').decode('CP1251', errors='replace'))

