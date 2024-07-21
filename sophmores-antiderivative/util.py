from scipy.integrate import quad

SUM_INF = 100
float_epsilon = 1e-3

integrate = lambda f, a, b: quad(f, a, b)[0]
summate = lambda f, a, b: sum(map(f, range(a, b + 1)))

feq = lambda a, b: abs(a - b) < float_epsilon
