from fractions import Fraction

a = [Fraction(1), Fraction(1)]

for i in range(40):
    x, y = a[-2], a[-1]
    a.append(1 + y / x)

for i in range(5, len(a)-1):
    # print("Error:", abs(a[i] - 2))
    print("Rate:", float(abs((a[i+1] - 2) / (a[i] - 2))))
