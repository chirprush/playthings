# 2x + 3(n - x) = 0 (mod 5)
# -x + 3n = 0 (mod 5)
# x = 3n (mod 5)
# n = 15
# x = 0 (mod 5)
# the sum of n choose x over all such x
# = 15 choose 0 + 15 choose 5 + 15 choose 10 + 15 choose 15
# = 6008

# heh funny name innit
head_count = {0: 0, 5: 0, 10: 0, 15: 0}

count = 0
for i in range(0, 2 ** 15):
    heads = bin(i).count('1')
    tails = 15 - heads
    if (2 * heads + 3 * tails) % 5 == 0:
        assert heads in head_count
        head_count[heads] += 1
        print("heads, tails", heads, tails)
        count += 1

print(count)
print(head_count)
