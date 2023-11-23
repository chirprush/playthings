# Too slow
N = 10 ** 4
M = 10 ** 9 + 7
total = 0

for k in range(1, N + 1):
    l = k ** 2 % M
    total += (l - 1) * ((1 - l) ** N % M - 1) // l % M

print(total)
