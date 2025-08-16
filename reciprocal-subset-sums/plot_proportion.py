import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

dom = np.arange(1, 33)

data = np.array([
    0.5,
    0.5,
    0.5,
    0.4375,
    0.40625,
    0.390625,
    0.351562,
    0.320312,
    0.292969,
    0.268555,
    0.245117,
    0.224365,
    0.205933,
    0.18988,
    0.174774,
    0.160919,
    0.1483,
    0.136803,
    0.126272,
    0.116635,
    0.107833,
    0.0997443,
    0.0923132,
    0.0854792,
    0.0791913,
    0.0734003,
    0.0680642,
    0.0631422,
    0.0585995,
    0.0544035,
    0.0505256,
    0.0469396
])

model = linregress(dom[5:], np.log(data)[5:])

mult = np.exp(model.intercept)

print(f"Model: y = ({mult}) * exp({model.slope} t)")
print(f"R-squared: {model.rvalue ** 2}")
print(f"p-value: {model.pvalue}")

f = lambda d: mult * np.exp(model.slope * d)
ext = np.linspace(1, 40, 1000)

plt.plot(dom, data, "bo")
plt.plot(ext, f(ext), "r")

plt.xlabel("$n$")
plt.ylabel("$P(X_n < 1)$")

plt.show()
