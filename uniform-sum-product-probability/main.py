from math import prod, factorial
from random import uniform

N = 10000
condition = 0

n = 2

for i in range(N):
    random_sum = sum(uniform(0, 1) for k in range(n))
    if random_sum >= 1:
        condition += 1
    # product = prod(uniform(0, 1) for k in range(n))
    # if product >= n ** (-n):
    #     condition += 1

print(f"Total cases:     {N}")
print(f"Fulfilled cases: {condition}")
print()
# For sums
print(f"Estimated probability: {condition / N}")
print(f"Exact probability:     {1 - 1 / factorial(n)}")
