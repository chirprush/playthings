from math import sqrt
from dataclasses import dataclass

@dataclass
class Vec3:
    x: int
    y: int
    z: int

    def add(self, other):
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def sub(self, other):
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def neg(self):
        return Vec3(
            -self.x,
            -self.y,
            -self.z
        )

    def mag(self, n):
        return Vec3(
            self.x * n,
            self.y * n,
            self.z * n
        )

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def norm(self):
        length = self.length()
        return Vec3(
            self.x / length,
            self.y / length,
            self.z / length
        )

@dataclass
class Ray:
    start: Vec3
    dir: Vec3

    def at(self, t):
        return self.start.add(self.dir.mag(t))
