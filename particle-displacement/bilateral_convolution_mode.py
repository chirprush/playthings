from math import factorial, comb

def H(t):
    if t >= 0:
        return 1
    return 0

# Hmm it doesn't seem to diverge that slowly? (Although if I put the values too
# high floating point precision errors seem to come in). The slower divergence is likely because
# the interval is twice as large compared to the shifted one on desmos.
# That being said, we have proved it to diverge mathematically anyways so I guess that doesn't matter
n = 40
r = 1/n

mode = 0

for k in range(0, n + 1):
    # We have subbed in t = 0
    mode += comb(n, k) * (-1) ** k * ((n - 2 * k) * r) ** (n - 1) * H((n - 2 * k) * r)

mode *= (2 * r) ** (-n) / factorial(n-1)

print(f"Mode: {mode}")
