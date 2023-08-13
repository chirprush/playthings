from math import floor, sqrt

def get_edge_algorithmic(n, b):
    for i in range(1, n):
        if b <= n - i:
            return (i, b + i)
        else:
            b -= n - i

def get_edge_mathematical(n, b):
    m = (n * (n - 1)) // 2 - b
    i = 1 + floor((n - 1) - 1 / 2 * (sqrt(1 + 8 * m) - 1))
    j = 1 + i + b - ((i - 1) * (2 * n - i)) // 2
    return (i, j)

N = 4
for b in range(1, N * (N - 1) // 2 + 1):
    print(get_edge_algorithmic(N, b), get_edge_mathematical(N, b - 1))
