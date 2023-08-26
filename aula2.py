import time
import matplotlib.pyplot as plt

x = []
y = []
problem_size = 1000000
print(f"{'problemSize':>12}{'Seconds':>16}")
for count in range(5):
    start = time.time()
    work = 1
    for _ in range(problem_size):
        work += 1
        work -= 1
    elapsed = time.time() - start
    print(f"{problem_size:>12}{elapsed:>16.3f}")
    x.append(problem_size)
    y.append(elapsed)
    problem_size *= 2

plt.plot(x, y)
plt.xlabel("Problem Size")
plt.ylabel("Time (Seconds)")
plt.title("Execution Time vs Problem Size")
plt.xscale("log")
plt.yscale("log")
plt.show()
