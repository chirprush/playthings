import numpy as np
import itertools as it

m = 3
k = 2

frequencies = {}

for i in range(m):
    frequencies[i] = 0

for data in it.product(*[list(range(m)) for _ in range(k ** 2)]):
    A = np.reshape(data, (k, k))

    frequencies[round(np.linalg.det(A)) % m] += 1

for i in frequencies:
    print(f"Class [{i}]: {frequencies[i]} element(s)")

print(f"Total: {sum(frequencies.values())} elements(s)")

print(f"f(0) - f(1) = {frequencies[0] - frequencies[1]}")
