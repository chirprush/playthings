from math import sqrt
from random import uniform
from statistics import mean, stdev
from scipy.integrate import quad
# Given 2 points in the unit cube, what is the expected value of the length?
# I'm sure you might be able to do this analytically, but let's use some fun
# stats and all that yeahhhhh.

# An interesting idea to think about is what happens if we change the
# dimensions of the square. If we scale it up by some factor A, does the
# distance scale up linearly with respect to A? Does it scale with respect to
# some power of A?
A = 1
# Empirically, this seems to scale linearly with A, but I'd like to have some
# way of showing such.

def uniform_point():
    return (uniform(0, A), uniform(0, A))

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def squared_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

distances = []
squared_distances = []

SAMPLES = 100000

for _ in range(SAMPLES):
    a = uniform_point()
    b = uniform_point()
    distance = dist(a, b)
    squared_distance = squared_dist(a, b)

    distances.append(distance)
    squared_distances.append(squared_distance)

print(f"Distance Mean:     {round(mean(distances), 4)}")
print(f"Distance Std Dev.: {round(stdev(distances), 4)}")

print(f"Squared Distance Mean:     {round(mean(squared_distances), 4)}")
print(f"Squared Distance Std Dev.: {round(stdev(squared_distances), 4)}")

# Ok I guess the analytical methods are a whole lot more interesting aren't
# they lol.

# Looks like the rough results (for normal distance) are
# Mean:     0.52
# Std dev.: 0.24
I = quad(lambda x1: quad(lambda y1: quad(lambda x2: quad(lambda y2: sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 0, A)[0], 0, A)[0], 0, A)[0], 0, A)[0]
print(f"Exact Average Distance: {round(I, 6)}")

# Note that for the squared distance, it's trivial to evaluate the quadruple
# integral and see that it's equal to 1/3.
