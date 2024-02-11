from random import randint

def run():
    s = 0
    t = 1

    while (s <= 0):
        s += randint(-1, 1)
        t += 1

    return t

t = 0
n = 1000

for i in range(n):
    t += run()

print("Approximate expected time:", t / n)
