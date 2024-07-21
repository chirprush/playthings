from math import floor, log2
from time import sleep
import numpy as np
from scipy.sparse import csr_matrix, identity

# There isn't really a builtin way to take the element-wise modulo of a
# csr_matrix, so we sorta have to define it here. Note that eliminating the
# zeros is important so that we don't accrue any unneeded slots in the matrix.
def mod_csr_matrix(M, modulus):
    M.data = M.data % modulus
    M.eliminate_zeros()
    return M

# The size of the matrix/definition of recurrence
N = 2000

# The kth value in the sequence
K = 10 ** 18

# The modulus under which we're looking for the answer
M = 20092010

# The number of digits in k, corresponding to the number of squares of matrices
# we need to create.
D = 1 + floor(log2(K))

inp = np.ones((N, 1), np.uint32)
T = csr_matrix((N, N), dtype=np.uint32)

T[0, N-1] = 1
T[0, N-2] = 1

for i in range(N-1):
    T[i+1, i] = 1

# Based
bases = []

for i in range(D):
    if i == 0:
        bases.append(T)
    else:
        T_ = mod_csr_matrix(bases[i - 1] ** 2, M)
        bases.append(T_)
    print(f"Created base matrix {i + 1}")
    sleep(0.1)

digits = bin(K)[2:][::-1]
t = identity(N, dtype=np.uint32, format="csr")

for i in range(D):
    if digits[i] == "1":
        t = mod_csr_matrix(t * bases[i], M)


print((t * inp)[N - 1, 0])
