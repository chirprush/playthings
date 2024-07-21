from gmpy2 import mpc

with open("roots.txt", "r") as roots_file:
    roots = [mpc(line.strip()) for line in roots_file.readlines()]

with open("coefficients.txt", "r") as coefficients_file:
    coefficients = [mpc(line.strip()) for line in coefficients_file.readlines()]

n = 1e+18

# Good old nan+nanj
# I could try and play around with the math a little to find some
# way to get modular arithmetic stuff to help, but it's pretty
# much back to the drawing board for this one. Maybe I should try
# and look for patterns in the sequence itself.
print(sum(coefficients[i] * roots[i] ** n for i in range(2000)))
