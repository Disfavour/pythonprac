import sys


data = "123приветabc"
print(type(data))
data = data.encode()
data = bytes(data)
print(type(data))
sys.stdout.buffer.write(data)
print(data)
print(float(data[0]))
data = data.decode()
print(data[0])
