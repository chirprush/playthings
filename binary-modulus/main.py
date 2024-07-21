# Source: AMC 10B 2022 Problem #25
# (In other words the thing I failed lol)
# For some reason, some of the later problems in the AMC are some of the easiest for me
# Probably because they're just more of what I work with usually, but idk. For some
# reason I can't wrap my head around geometry and I have a lot of trouble with
# accurately interpreting probability and combinatorics sometimes.

# Let S_n = \sum_{k = 0}^{n - 1} x_k 2^k, where x_k is a sequence of either 0s or 1s
# Suppose that for all n >= 1, 7 * S_n = 1 (mod 2^n), can we find a closed form for
# x_n? I won't be doing that here, but I want to check some work that I very much
# believe is wrong but don't know why.

# YOOOO IT WAS RIGHT

# Using some fun summation stuff, we can make and solve a recurrence to find that
# x_{n+3} = x_n. The only thing I was confused about was why this wasn't true for
# 0 <= n <= 2, but it turns out that those are because there were some conditions
# for using the n in the summations. Maybe I'll write something for this.

n = 0

for i in range(1, 20):
    add = 2 ** (i - 1)
    if 7 * (n + add) % 2 ** i == 1:
        print(1, end="")
        n += add
    elif 7 * n % 2 ** i == 1:
        print(0, end="")

print()
