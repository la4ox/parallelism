import subprocess
import sys
import time

N = 8
t0 = time.perf_counter()

processes = []

for i in range(N):
    p = subprocess.Popen(
        [sys.executable, "sum_subprocess_worker.py", str(i), str(N)],
        stdout=subprocess.PIPE,
        text=True
    )
    processes.append(p)

s = 0

for p in processes:
    out, _ = p.communicate()
    s += int(out)

t1 = time.perf_counter()

print((t1-t0), s)
