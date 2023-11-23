# Verification of an identity a friend gave for the number of ways one may roll k dice to get n
from math import comb

def choose(n, k):
    if n < k or n < 0:
        return 0
    return comb(n, k)

def solution1(n, k):
    return sum((-1) ** m * choose(k, m) * choose(n - 6 * m - 1, k - 1) for m in range(k + 1))

# The first solution one might reach for when tackling programming this problem
# is dynamic programming. We have that:
# f(n, 1) = 1 for 1 <= n <= 6,
# f(n, k) = Sum[f(n - m, k - 1), {m, 1, 6}]
def solution2(n, k):
    if k > n:
        return 0

    N = max(n, k, 6)

    # Due to indexing and all that we have that f(n, k) = A[n - 1, k - 1]
    A = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]

    for m in range(6):
        A[m][0] = 1

    # Honestly a bit dirty looking but hey hey
    for m in range(1, k):
        for l in range(N):
            for a in range(1, 7):
                if l - a >= 0:
                    A[l][m] += A[l - a][m - 1]

    return A[n - 1][k - 1]

# Looks like everything checks out
for n in range(51):
    for k in range(1, 51):
        if (solution1(n, k) != solution2(n, k)):
            print(f"Discrepancy: {(n, k)}")
