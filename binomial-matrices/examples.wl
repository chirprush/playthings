B[n_] := Table[Binomial[i - 1, j - 1], {i, 1, n + 1}, {j, 1, n + 1}]

Print[B[2]]
Print[B[2] . Transpose[B[2]]]
Print[Transpose[B[2]] . B[2]]
Print[Eigensystem[B[2]]]

Print[B[3] . Transpose[B[3]] // MatrixForm]
