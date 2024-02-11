def count(n, s = 0):
    if n == 0:
        return int(s > 0)
    elif s > 0:
        return 0

    c = 0
    for i in [-1, 1]:
        c += count(n - 1, s + i)

    return c

def count_zero(n, s = 0):
    if n == 0:
        return int(s > 0)
    elif s > 0:
        return 0

    c = 0
    for i in [-1, 0, 1]:
        c += count_zero(n - 1, s + i)

    return c

# For n = 2k - 1, this function is the kth Catalan number
# For n = 2k, this function is 0
print([count(i + 1) for i in range(10)])

# This is the doubled Catalan number sequence, or the ceil(n/2)th Catalan
# number
print([count_zero(i + 1) for i in range(10)])

# Quite interesting actually
