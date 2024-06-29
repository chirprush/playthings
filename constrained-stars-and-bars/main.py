from cmath import exp, pi
from math import prod

constrains = [5, 5, 5] 
k = len(constrains)
n = 5
N = 2 * n + 1

def gen(x):
    # Probably won't be called due to floating point rounding stuff but hey
    if x == 1:
        return prod(r + 1 for r in constrains)

    return prod(x ** (e + 1) - 1 for e in constrains) / (x - 1) ** k

a = exp(2j * pi / N)

result = 0

# Wait is this even correct? Should it output 36?
for j in range(N):
    result += gen(a ** j) * a ** (-n * j)

result /= N

print(result.real)
