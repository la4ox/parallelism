import os
import time
import multiprocessing as mp


INT_SIZE = 4
filename = "data.bin"


def calc_sum(args):
    k, n = args
    size = os.path.getsize(filename)
    chunk = size // n

    local = 0
    with open(filename, "rb") as f:
        f.seek(k * chunk)
        for _ in range(chunk // INT_SIZE):
            local += int.from_bytes(f.read(INT_SIZE), "big")

    return local


if __name__ == "__main__":
    t0 = time.perf_counter()

    with mp.Pool(INT_SIZE) as pool:
        parts = pool.map(calc_sum, [(i, INT_SIZE) for i in range(INT_SIZE)])

    s = sum(parts)
    t1 = time.perf_counter()

    print((t1 - t0), s)
