from math import e
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def diff(self, other):
        return Point(self.x - other.x, self.y - other.y)

points = [
    Point(1/e, -1),
    Point(1, 0),
    Point(e, 1),
    Point(e ** 2, 2),
    Point(e ** 3, 3),
]

@dataclass
class Spline:
    i: int
    a: float
    b: float
    c: float

    def from_prev(i, b, c, d):
        return Spline(
            i,
            b / d.x - c / d.x ** 2 + d.y / d.x ** 3,
            -2 * b + 3 * c / d.x - 3 * d.y / d.x ** 2,
            b * d.x - 2 * c + 3 * d.y / d.x
        )

    def latex(self):
        # Apparently f-strings don't support backslashes (probably for good reason)
        cmd = lambda s: "\\" + s
        if points[self.i].x == 0:
            monomial = f"x"
        elif points[self.i].x < 0:
            monomial = f"{cmd('left')}( x + {abs(points[self.i].x):0.8f} {cmd('right')})"
        else:
            monomial = f"{cmd('left')}( x - {points[self.i].x:0.8f} {cmd('right')})"
        return f"f_{self.i} {cmd('left')}( x {cmd('right')}) = {self.a:0.8f} {monomial}^3 + {self.b:0.8f} {monomial}^2 + {self.c:0.8f} {monomial} + {points[self.i].y:0.8f} {cmd('left')}{cmd('{')} {points[self.i].x:0.8f} {cmd('le')} x {cmd('le')} {points[self.i + 1].x:0.8f} {cmd('right')}{cmd('}')}"

    def desmos(self):
        cmd = lambda s: "\\" + s
        if points[self.i].x == 0:
            monomial = f"x"
        elif points[self.i].x < 0:
            monomial = f"(x + {abs(points[self.i].x):0.8f})"
        else:
            monomial = f"(x - {points[self.i].x:0.8f})"
        return f"f_{self.i}(x) = {self.a:0.8f}{monomial}^3 + {self.b:0.8f}{monomial}^2 + {self.c:0.8f}{monomial} + {points[self.i].y:0.8f} {cmd('left')}{cmd('{')}{points[self.i].x:0.8f} {cmd('le')} x {cmd('le')} {points[self.i + 1].x:0.8f}{cmd('right')}{cmd('}')}"

n = len(points)

splines = []

initial_b, initial_c = 0, 0
initial_d = points[n - 1].diff(points[n - 2]) # heh
initial_a = (initial_d.y - initial_c * initial_d.x - initial_b * initial_d.x ** 2) / initial_d.x ** 3

splines.append(Spline(n - 2, initial_a, initial_b, initial_c))

for k in range(1, n - 1):
    i = n - 2 - k
    diff = points[i + 1].diff(points[i])
    splines.append(Spline.from_prev(i, splines[k - 1].b, splines[k - 1].c, diff))

splines.reverse()

print("\\begin{align*}")
for s in splines:
    print("  " + s.latex() + " \\\\")
print("\\end{align*}")
