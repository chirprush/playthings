# A small program to calculate convergents for some continued fraction
# representation

# Let p(n) be the numerator and q(n) be the denominator of the continued
# fraction. We may use the following recurrence to calculate subsequent numerators and denominators:
# p(n) = a(n) p(n - 1) + p(n - 2)
# q(n) = a(n) q(n - 1) + q(n - 2),
# where a(n) is the continued fraction representation

# The continued fraction representation for e
def a(k):
    if k == 0:
        return 2
    elif k % 3 == 2:
        return 2 * (k // 3 + 1)
    return 1

p1, p2 = 2, 3
q1, q2 = 1, 1

N = 100

for n in range(2, N):
    p_new = a(n) * p2 + p1
    q_new = a(n) * q2 + q1

    p1, p2 = p2, p_new
    q1, q2 = q2, q_new

print(f"{p_new}/{q_new}")
