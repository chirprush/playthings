import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def f(z):
    return z ** 2000 - z - 1

re, im = np.mgrid[-1.1:1.1:1000j, -1.1:1.1:1000j]

fig, ax = plt.subplots()

ax.set_title("Lazy Domain Coloring for the Characteristic Polynomial $r^{2000} - r - 1$")
ax.set_xlabel(r"$\mathcal{R} \left( z \right)$")
ax.set_ylabel(r"$\mathcal{I} \left( z \right)$")

plt.imshow(abs(f(re + 1j * im).T), cmap="gray", vmin=0, vmax=2)

plt.show()

# I tried graphing some complex functions as well as the characteristic polynomial, but
# it didn't go the best. To be honest, I didn't expect much though (after all I
# can't find good values for the roots by just looking at a crude graph of
# them). Luckily, Wolfram comes to the rescue, and now I have super accurate estimates
# for all 2000 roots. I have so much power now.
