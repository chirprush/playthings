import numpy as np
from PIL import Image

colors = [
    0x222436,
    0x82aaff,
    0x86e1fc,
    0xc8d3f5,
    0xc3e88d,
    0xc099ff
]

nodes = []

for i in colors:
    r, g, b = i >> 16, (i >> 8) & 0xff, i & 0xff
    nodes.append(np.array([r, g, b], dtype=np.float64) / 0xff)

with Image.open("blue-source.png") as src:
    pixels = np.array(src)

    for i in range(pixels.shape[0]):
        print(f"Progress: {round(100 * (i + 1) / pixels.shape[0], 1)}")
        for j in range(pixels.shape[1]):
            sv = np.array(pixels[i, j])
            x = pixels[i, j] / 0xff

            result = np.array([0, 0, 0], dtype=np.float64)

            for p in nodes:
                C, n, a = 1, 1, 3.5
                r = np.sqrt(np.dot(p - x, p - x))

                result += C * r ** n * np.exp(-a * r) * (p - x)

            x += result

            pixels[i, j] = np.round(x * 0.75 * 0xff)

    res = Image.fromarray(pixels)
    res.show()
