alpha1 = 0.0006
alpha2 = 3.852
beta1 = 0.260
beta2 = 0.02

V = 9.3 * 10 ** 9

x = [V, 100]

for i in range(1000):
    dt = 0.1

    T, H = x
    x = [T + dt * (alpha1 * (V - T) - beta1 * H), H + dt * (alpha2 * (V - T) + beta2 * H)]

    print(x)
