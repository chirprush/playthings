from math import sqrt
from statistics import mean, stdev

def corner(a, b):
    a, b = min([a, b], key=lambda p: p[0]), max([a, b], key=lambda p: p[0])
    i_x, i_y = b[0], a[1]
    x = 1 / 2  * (i_x - i_y + sqrt(2 - (i_x - i_y) ** 2))
    y = x - i_x + i_y
    return (x, y)

points = [(0, 1), (1, 0)]

n = 5

for _ in range(n):
    new_points = [points[0]]
    for i in range(1, len(points)):
        new_points.append(corner(points[i - 1], points[i]))
        new_points.append(points[i])

    points = new_points

print("Points:", len(points))
print("Approximation:", 4 * sum(points[i][1] * (points[i + 1][0] - points[i][0]) for i in range(len(points) - 1)))
print()

xdiffs = [points[i + 1][0] - points[i][0] for i in range(len(points) - 1)]
print("Average of x-differences:", mean(xdiffs))
print("Std dev. of x-differences:", stdev(xdiffs))
print("Range of x-differences:", max(xdiffs) - min(xdiffs))
print(max(((i, xdiffs[i]) for i in range(len(xdiffs))), key=lambda t: t[1]))

# Empirically it does seem to check out to approximate pi and this time around
# I made sure that the recurrence was correct by checking the number of points:
# Points: 1048577
# Approximation: 3.1430271877389186
# It still isn't terribly efficient though, mostly because the number of points grows exponentially with respect to n.
# It seems the range of the xdiffs goes down as n gets bigger, so one really
# could make the argument that this approaches the integral of sqrt(1-x^2); I
# just don't really know how to rigorously show that.
