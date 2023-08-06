start = 4
end = 6

rectangles = 100

dx = (end - start) / rectangles

def f(x):
    return 5 / x

sum_ = 0

for i in range(rectangles):
    sum_ += dx * f((i + 1) * dx + start)

print(sum_)
