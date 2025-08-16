import numpy as np
# import galois

# Seems to hold for 2x2 matrices
p = 5
# GF = galois.GF(p)

def check_polynomial(A, B):
    for a in range(p):
        for b in range(p):
            one_way = np.array_equal((a * A + np.array([[b, 0], [0, b]])) % p, B)
            other_way = np.array_equal((a * B + np.array([[b, 0], [0, b]])) % p, A)

            if one_way or other_way:
                return True

    return False

matrices = []

for a in range(p):
    for b in range(p):
        for c in range(p):
            for d in range(p):
                matrices.append(np.array([[a, b], [c, d]]))

count = 0

for A in matrices:
    for B in matrices:
        if np.array_equal((A @ B) % p, (B @ A) % p) and not check_polynomial(A, B):
            print(A)
            print(B)
