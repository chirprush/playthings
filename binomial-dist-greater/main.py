from scipy.stats import binom
from math import comb

# The probability should be 1/2 - 1 / 2^(2n) nCr(2n - 1, n), no?
p = 0.5
n = 10

total = 10000
success_trials = 0

for trials in range(total):
    x = binom.rvs(n, p)
    y = binom.rvs(n, p)

    if x > y:
        success_trials += 1

# Simulated
print(success_trials / total)

# My answer
print(1 / 2 - 1 / (2 ** (2 * n)) * comb(2 * n - 1, n))

# MSE Answer
print(1 / 2 - 1 / (2 ** (2 * n + 1)) * comb(2 * n, n))

# Would you look at that you know what that makes a whole lot of sense
