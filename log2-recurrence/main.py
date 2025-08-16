from fractions import Fraction

def M(n):
    return 2 ** (n.bit_length() - 1)

N = 20
a = [Fraction(0)] * (N + 1)
a[0] = Fraction(1)

for n in range(N + 1):
    m = M(n)
    a[n] = 1 + a[2 * M - (n + 1)] / a[n - M]

print(a)
