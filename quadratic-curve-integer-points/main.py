import matplotlib.pyplot as plt
from math import sqrt, ceil, floor, cos, sin, pi, log
from scipy.integrate import quad
from sklearn.linear_model import LinearRegression
import numpy as np

c = quad(lambda theta: 0.5 / (1 - cos(theta) * sin(theta)), 0, 2 * pi)[0]

def is_square(n):
    x = int(round(sqrt(n)))

    return x * x == n

# Count the number of Eisenstein integers with norm less than or equal to r
def count_all(r):
    left = ceil(- sqrt(4 * r / 3))
    right = floor(sqrt(4 * r / 3))

    total = 0

    for x in range(left, right + 1):
        up = floor((x + sqrt(4 * r - 3 * x * x)) / 2)
        down = ceil((x - sqrt(4 * r - 3 * x * x)) / 2)

        total += int(up - down + 1)

    return total

levels = [2 ** i for i in range(40)]
errors = []

for i in range(len(levels)):
    count = count_all(levels[i])
    estimate = c * levels[i]
    error = abs(count - c * levels[i])

    errors.append(error)

    print(f"Actual: C(levels[i]) = {count}")
    print(f"Estimated: c(levels[i]) = {estimate}")
    print(f"Error: {error}")
    print()

plt.xscale("log")
plt.yscale("log")

inp = np.array([log(i) for i in levels]).reshape(-1, 1)
out = [log(i) for i in errors]

reg = LinearRegression().fit(inp, out)

pred = reg.predict(inp)

plt.plot(np.exp(inp.reshape(len(inp))), np.exp(pred))

print(f"Regression score: {reg.score(inp, out)}")
print(f"E(r) = {reg.intercept_} * r^{reg.coef_[0]}")

plt.plot(levels, errors, "bo")


plt.show()
