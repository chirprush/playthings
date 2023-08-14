from math import sqrt
from statistics import mean, stdev

def corner(a, b):
    a, b = min([a, b], key=lambda p: p[0]), max([a, b], key=lambda p: p[0])
    i_x, i_y = b[0], a[1]
    x = 1 / 2  * (i_x - i_y + sqrt(2 - (i_x - i_y) ** 2))
    y = x - i_x + i_y
    return (x, y)

points = [(0, 1), (1, 0)]

n = 20

for _ in range(n):
    new_points = [points[0]]
    for i in range(1, len(points)):
        new_points.append(corner(points[i - 1], points[i]))
        new_points.append(points[i])

    points = new_points

print("Points:", len(points))# , points)
print("Approximation:", 4 * sum(points[i][1] * (points[i + 1][0] - points[i][0]) for i in range(len(points) - 1)))
print()

xdiffs = [points[i + 1][0] - points[i][0] for i in range(len(points) - 1)]
print("Average of x-differences:", mean(xdiffs))
print("Std dev. of x-differences:", stdev(xdiffs))
print("Range of x-differences:", max(xdiffs) - min(xdiffs))
max_index, max_width = max(((i, xdiffs[i]) for i in range(len(xdiffs))), key=lambda t: t[1])
min_index, min_width = min(((i, xdiffs[i]) for i in range(len(xdiffs))), key=lambda t: t[1])
print("(Max Index, Max Width)", (max_index, max_width))
print("(Min Index, Min Width)", (min_index, min_width))
print("Min Width/Max Width", min_width / max_width)

exit()

# In the case that you would like to generate a diagram for S_n, here you go
with open(f"gen/diagram{n}.tex", "w") as f:
    f.write("\\documentclass{standalone}\n")
    f.write("\\usepackage{tikz}\n\n")
    f.write("\\begin{document}\n")
    f.write("\\begin{tikzpicture}[scale=4]\n")

    f.write("\\node at (0.5, -0.1) {\\small \\( n = %d \\)};\n" % n)
    f.write("\\draw (1, 0) arc (0:90:1);\n")
    f.write("\\draw[->] (-0.05, 0) -- (1.2, 0);\n")
    f.write("\\draw[->] (0, -0.05) -- (0, 1.2);\n")

    for i in range(len(points)-1):
        options = "[blue]" if i == min_index else ""
        f.write("\\draw %s -- (%f, %f);\n" % (repr(points[i]), points[i+1][0], points[i][1]))
        f.write("\\draw (%f, %f) -- %s;\n" % (points[i+1][0], points[i][1], repr(points[i+1])))
        f.write("\\fill%s %s circle (0.005);\n" % (options, repr(points[i])))
    f.write("\\fill %s circle (0.005);\n" % repr(points[len(points) - 1]))

    f.write("\\end{tikzpicture}\n")
    f.write("\\end{document}\n")
# Empirically it does seem to check out to approximate pi and this time around
# I made sure that the recurrence was correct by checking the number of points:
# Points: 1048577
# Approximation: 3.1430271877389186
# It still isn't terribly efficient though, mostly because the number of points
# grows exponentially with respect to n. It seems the range of the xdiffs goes
# down as n gets bigger, so one really could make the argument that this
# approaches the integral of sqrt(1-x^2); I just don't really know how to
# rigorously show that.
