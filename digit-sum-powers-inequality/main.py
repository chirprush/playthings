def digit_sum(n):
    s = 0

    while n:
        s += n % 10
        n //= 10

    return s

for i in range(1, 51):
    d5 = digit_sum(5 ** i)
    d2 = digit_sum(2 ** i)
    if d5 == d2:
        print(f"d(5^{i}) = d(2^{i})")
    elif d5 < d2:
        print(f"d(5^{i}) < d(2^{i})")
    else:
        print(f"d(5^{i}) > d(2^{i})")


# Question: is there an efficient way to compute digit sums of powers without having to
# physically expand them out?
