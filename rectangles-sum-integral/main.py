def exact_sum(w, h):
    return sum(
        (w + 1 - i) * (h + 1 - j)
        for i in range(1, w + 1)
        for j in range(1, h + 1)
    )

# Lmao I forgor I could just use double sums
def closed_form(w, h):
    return 1 / 4 * w * h * (w + 1) * (h + 1)

def integral_approximation(w, h):
    return w * h * (w + 1) * (h + 1) - 1/2 * w ** 2 * h * (h + 1) - 1/2 * w * h ** 2 * (w + 1) + 1 / 4 * w ** 2 * h ** 2

pairs = [
    (3, 2), (2, 3),
    (1, 3), (5, 2),
    (4, 6), (13, 17)
]

for (w, h) in pairs:
    exact = exact_sum(w, h)
    approximation = integral_approximation(w, h)
    closed = closed_form(w, h)
    error = round((approximation - exact) / exact * 100, 2)
    print(f"Exact:        {exact}")
    print(f"Closed:       {closed}")
    print(f"Approxmation: {approximation}")
    print(f"Error:        {error}%")
    print()
