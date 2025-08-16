def classify(n):
    sieve = [False] * (n + 1)
    orders = {}

    for k in range(2, n + 1):
        if sieve[k]:
            continue

        e = k
        i = 0

        while e <= n:
            sieve[e] = True
            e = e * e
            i += 1

        order = 2 ** i

        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1

    return orders

for i in range(2, 18):
    print(f"D^{i} (F_2) ~= {classify(i)}")
