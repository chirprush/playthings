import numpy as np

A = np.array([
    [3,  1, 0,  0, 0],
    [3,  5, 8,  0, 0],
    [0, 16, 3,  4, 0],
    [0,  0, 2,  2, 3],
    [0,  0, 0, 10, 6]
])

n = A.shape[0]

print("Determinant (numpy):", np.linalg.det(A))

d = [0] * n
d[0] = A[0][0]

D = d[0]

for i in range(1, n):
    d[i] = A[i][i] - A[i][i - 1] * A[i - 1][i] / d[i - 1]
    D *= d[i]

print("Determinant (theoretical):", D)
