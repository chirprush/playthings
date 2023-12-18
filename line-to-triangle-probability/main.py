from random import uniform

# Randomly break a line segments of length 1 into three smaller segments. What
# is the probability that it forms a valid triangle?

# Let's empirically find out the answer and test some different methods.

N = 1000

def valid_triangle(a, b, c):
    return (a <= b + c) and (b <= a + c) and (c <= a + b)

# This method uses normalization to guarantee that they all add up to one
# Turns out that this method is not uniform (see https://stackoverflow.com/questions/8064629/random-numbers-that-add-to-100-matlab/8068956#8068956)
def method1():
    valid = 0

    for i in range(N):
        l1, l2, l3 = uniform(0, 1), uniform(0, 1), uniform(0, 1)
        
        a, b, c = l1 / (l1 + l2 + l3), l2 / (l1 + l2 + l3), l3 / (l1 + l2 + l3)

        if valid_triangle(a, b, c):
            valid += 1

    return valid / N

# This method picks the values uniformly across [0,1] and then builds lengths
# out of them. This is indeed uniform (after all we've defined it as such) and
# it also is quite easy to work with mathematically when transforming into
# random variables.
def method2():
    valid = 0

    for i in range(N):
        x1 = uniform(0, 1)
        x2 = uniform(0, 1)

        a = min(x1, x2)
        b = max(x1, x2)

        if valid_triangle(a, b - a, 1 - b):
            valid += 1

    return valid / N

print("Method 1: ", method1())
print("Method 2 (correct): ", method2())
