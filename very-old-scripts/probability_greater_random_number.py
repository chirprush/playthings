# What is the probability that, taking two random numbers from a set of n (in
# this case 8) consecutive integers, the first number will be greater than the
# second? I would think 1/2, but I don't know any probability lol

from random import randint

samples = 10_000_000

were_greater = 0

for _ in range(samples):
    if randint(1, 2) < randint(1, 2):
        were_greater += 1

print(f"{were_greater}/{samples} cases had the first number greater than the second.")
print(f"Probability: {were_greater/samples}")

# The real probability should be something like
# P(a > b) =
# P(a = 1) * P(b < 1) + 
# P(a = 2) * P(b < 2) + 
# P(a = 3) * P(b < 3) + 
# P(a = 4) * P(b < 4) + 
# P(a = 5) * P(b < 5) + 
# P(a = 6) * P(b < 6) + 
# P(a = 7) * P(b < 7) + 
# P(a = 8) * P(b < 8)
# where a, b in {1..8}

# P(a,b = k) is just 1/8
# P(a,b < k) is just (k - 1)/8

# so, the final probability is
# P(a > b) =
# 1/8 * 0/8 + 
# 1/8 * 1/8 + 
# 1/8 * 2/8 + 
# 1/8 * 3/8 + 
# 1/8 * 4/8 + 
# 1/8 * 5/8 + 
# 1/8 * 6/8 + 
# 1/8 * 7/8
# = 1/64 * (7 * 8 / 2) <- factoring out a 1/8 and using triangle numbers
# = 1/64 * 28
# = 14/32
# = 7/16 
# = 0.4375
# and we do see this with the estimated probability
