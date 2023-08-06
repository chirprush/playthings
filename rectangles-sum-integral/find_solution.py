from math import sqrt, floor

distances = []

for w in range(1, 2_000_000):
    a = 8_000_000 / (w * (w + 1))
    h = floor(1/2 * (-1 + sqrt(4 * a + 1)))

    dist1 = 2_000_000 - 1 / 4 * w * (w + 1) * h * (h + 1)
    dist2 = 2_000_000 - 1 / 4 * w * (w + 1) * (h + 1) * (h + 2)

    # if (dist1 >= 0):
    distances.append((w, h, abs(dist1)))
    # if (dist2 >= 0):
    distances.append((w, h + 1, abs(dist2)))

print(min(distances, key=lambda a: a[2]))
