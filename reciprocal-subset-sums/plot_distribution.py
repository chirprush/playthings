import matplotlib.pyplot as plt

n = 15
data = [0]

for i in range(1, n + 1):
    k = len(data)

    for j in range(k):
        data.append(data[j] + 1 / i)

print("Actual Mean:", sum(data) / len(data))
print("Theoretical Mean:", sum(1/(2 * i) for i in range(1, n + 1)))

plt.hist(data, 200, density=True)

plt.xlabel("Subset Sum")
plt.ylabel("Probability")

plt.show()

# Of course, the mean is H_n / 2 and the variance is bounded above by pi^2 / 24
# Bounds given by Chebyshev and the like kinda suck
# Maybe try Chernoff's bound? What even is the moment generating function here
# rbo

# Is the random variable even well defined in the limit? If not, we have to
# probably consider some sort of normalization factor (probably like 1/n since
# that definitely will converge).
