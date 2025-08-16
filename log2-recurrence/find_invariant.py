from sympy import Poly, symbols, simplify, expand

deg = 4

p_coeff = [symbols(f"p{i}") for i in range((deg + 2) * (deg + 1) // 2)]
q_coeff = [symbols(f"q{i}") for i in range((deg + 2) * (deg + 1) // 2)]

x, y = symbols("x y")

def construct(coeffs, x, y):
    total = 0
    counter = 0

    for i in range(deg + 1):
        for j in range(deg - i + 1):
            total += coeffs[counter] * x ** i * y ** j
            counter += 1

    return total

P = construct(p_coeff, x, y)
Q = construct(q_coeff, x, y)

result = P * Q.subs({x: y, y: 1 + y/x}) - Q * P.subs({x: y, y: 1 + y / x})
form = Poly(expand(x ** deg * result), *p_coeff, *q_coeff)

print(form.subs({x: 1, y: 1}))

# Yeah this won't really yield much at all
