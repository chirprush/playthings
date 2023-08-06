# Let's simplify the problem (making the numbers smaller):
# We have 6 colors, with each color having 2 balls each
# We want to figure out how many ways to choose without replacement 4 balls
# having k distinct ball colors
def get_color(index: int):
    return index // 2

K = 3
condition = 0
total = 0

for i in range(12):
    for j in range(12):
        for k in range(12):
            for l in range(12):
                if len(set([i, j, k, l])) == 4:
                    total += 1
                    if len(set(get_color(a) for a in [i, j, k, l])) == K:
                        condition += 1

print(f"Total:     {total}")
print(f"Condition: {condition}")
