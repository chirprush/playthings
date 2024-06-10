from itertools import combinations
from math import comb, gcd

def valid(n, m, c):
    counts = {i : 0 for i in range(n)}

    for t in c:
        for v in t:
            counts[v] += 1

    return all(counts[i] == m for i in range(n))

def g(s, k, n, m):
    chunks = list(combinations(range(n), k))
    candidates = combinations(chunks, s)

    count = 0

    for c in candidates:
        result = valid(n, m, c)
        count += int(result)

        # if result:
        #     print(c)

    return count

def f(n, k):
    count = 0

    k_ = k // gcd(n, k)
    for m in range(0, comb(n - 1, k - 1) + 1, k_):
        s = n * m // k
        count += g(s, k, n, m)

    return count

for n in range(1, 7):
    count = 4

    print(n, end=" ")

    print(2, end=" ")

    for k in range(1, n):
        result = f(n, k)
        print(result, end=" ")
        count += result

    print(2, end=" ")

    print(count)
