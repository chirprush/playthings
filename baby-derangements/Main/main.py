from itertools import permutations
from random import choice

n = 4
m = 100000
arrangements = list(permutations(range(0, n)))

def score(arrangement):
    return sum(1 for i in range(len(arrangement)) if arrangement[i] == i)

frequencies = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
total_score = 0

for _ in range(m):
    arrangement = choice(arrangements)
    s = score(arrangement)
    frequencies[s] += 1
    total_score += s

print("Total trials:", m)
print("Frequencies:")
for f in frequencies:
    print(f"  {f}: {frequencies[f]}")
print("Expected Matches:", total_score / m)
