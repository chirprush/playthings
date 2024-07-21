def zround(z, n=12):
    real = round(z.real, n)
    imag = round(z.imag, n)

    return complex(real, imag)

def zeq(z1, z2, e=1e-12):
    return abs(z1.real - z2.real) < e and abs(z1.imag - z2.imag) < e
