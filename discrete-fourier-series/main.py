# How the heck does a discrete Fourier transform work?
# (We don't really FFT right here)
import matplotlib
matplotlib.use("gtk3agg")

import matplotlib.pyplot as plt
import numpy as np
from cmath import pi, exp, sin, cos

N = 25
L = pi

def sample(n):
    x = 2 * n * L / N
    return sin(x)
    # return sin(x)

def dft(k):
    return sum(sample(n) * exp(-2j * pi * n * k / N) for n in range(N))

transformed = [dft(k) for k in range(N)]
domain = list(range(N))
sam = [sample(n) for n in range(N)]
real = [y.real for y in transformed]
imag = [y.imag for y in transformed]
mag = [abs(y) / N for y in transformed]

for k, a in enumerate(mag):
    print(k, a)

figure, axes = plt.subplots(4)
figure.suptitle("DFT of sin(x)")

axes[0].plot(domain, sam, color="purple", marker="o", linestyle="none")
axes[1].plot(domain, real, color="blue", marker="o", linestyle="none")
axes[2].plot(domain, imag, color="red", marker="o", linestyle="none")
axes[3].plot(domain, mag, color="green", marker="o", linestyle="none")

plt.show()

# That's pretty darn coolio I think I understand now
