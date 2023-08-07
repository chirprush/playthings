from math import sqrt
from random import uniform
from statistics import mean, stdev
# Given 2 points in the unit cube, what is the expected value of the length?
# I'm sure you might be able to do this analytically, but let's use some fun
# stats and all that yeahhhhh.

def uniform_point():
    return (uniform(0, 1), uniform(0, 1))

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

distances = []

SAMPLES = 100000

for _ in range(SAMPLES):
    a = uniform_point()
    b = uniform_point()
    distance = dist(a, b)

    distances.append(distance)

print(f"Mean:     {round(mean(distances), 4)}")
print(f"Std Dev.: {round(stdev(distances), 4)}")

# Ok I guess the analytical methods are a whole lot more interesting aren't
# they lol.

# Looks like the rough results are
# Mean:     0.52
# Std dev.: 0.24
