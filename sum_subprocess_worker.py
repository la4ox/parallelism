import sys
import os

INT_SIZE = 4
filename = "data.bin"

k = int(sys.argv[1])
n = int(sys.argv[2])

size = os.path.getsize(filename)
chunk = size // n

local_s = 0
with open(filename, "rb") as f:
    f.seek(k * chunk)
    for _ in range(chunk // INT_SIZE):
        local_s += int.from_bytes(f.read(INT_SIZE), "big")

print(local_s)
