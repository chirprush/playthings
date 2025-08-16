alpha1 := 0.024
alpha2 := 3.852
beta1 := 0.260
beta2 := 0.02

V := 9.3 * 10^9

A := {{-alpha1, -beta1}, {-alpha2, beta2}}
Ainv := Inverse[A]
b := {alpha1 * V, alpha2 * V}

L := MatrixExp[A * t]

x0 := {V, 2}

xt = -Dot[Ainv, b] + Dot[Ainv, L, b] + Dot[L, x0]

roots := NSolve[First[xt] == 0 && t > 0 && t < 30, t]
time := t /. roots[[1]]

Print[time]
Print[NIntegrate[365 * 2000 * Part[xt, 2], {t, 0, time}]]
