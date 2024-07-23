from math import sin, log, e, tau

sin_period = tau
sin_ln_period = e ** (sin_period)

step = 0.01

x = 0
while x <= sin_ln_period:
    try:
        value = sin(log(x, e))
    except ValueError:
        value = float("nan")
    print(f"{x:.2f}: {value:.4f}")
    x += step
