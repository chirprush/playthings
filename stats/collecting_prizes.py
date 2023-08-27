import matplotlib.pyplot as plt
from random import randint

N = 100
buckets = {}

for _ in range(N):
    prizes = [False, False, False, False]
    i = 0
    while not all(prizes):
        prizes[randint(0, 3)] = True
        i += 1
    buckets[i] = buckets.get(i, 0) + 1

X = buckets.keys()
Y = buckets.values()

print(buckets)
print(sum(x * y / N for (x, y) in buckets.items()))
# plt.xticks(list(range(min(X), max(X) + 1)))
# plt.yticks(list(range(0, max(Y) + 1)))
# 
# plt.bar(X, Y, 0.5, color='b')
# 
# plt.show()
