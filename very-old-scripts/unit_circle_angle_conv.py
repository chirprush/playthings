def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

class Frac:
    def __init__(self, num, den):
        d = gcd(num, den)
        self.num = num // d
        self.den = den // d

class Radians:
    def __init__(self, frac):
        self.frac = frac

    def degrees(self):
        return 180 // self.frac.den * self.frac.num

    def to_str(self):
        if self.frac.num == 0:
            return "0"
        num_part = (str(self.frac.num) if self.frac.num != 1 else "") + "π"
        den_part = ("/" + str(self.frac.den) if self.frac.den != 1 else "")
        return num_part + den_part

for i in range(0, 24):
    frac = Frac(i, 12)
    if frac.den == 12:
        continue
    rad = Radians(frac)
    print(f"{rad.to_str()},{rad.degrees()}")
