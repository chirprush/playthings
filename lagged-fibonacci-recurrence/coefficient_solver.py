import numpy as np

with open("roots.txt", "r") as roots_file:
    roots = np.array([complex(line.strip()) for line in roots_file.readlines()])

equations_matrix = np.fromfunction(
    lambda row, col: roots[col.astype(int)] ** row,
    (2000, 2000)
)

solutions_matrix = np.ones(2000)

# I'm somewhat worried due to the floating errors for powers
# but what can you do

coefficients = np.matmul(
    np.linalg.inv(equations_matrix),
    solutions_matrix
)

np.savetxt("coefficients.txt", coefficients)
