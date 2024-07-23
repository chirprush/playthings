# An interesting question from Rishan, what does the graph of x ^ x look when x < 0?

def f(num, den):
    base = -num / den
    # we need to do this instead of just base ** base because python no likey
    # discrete exponents
    result = (base ** (-num)) ** (1 / den)
    # oh boy don't you just love computer float math
    if isinstance(result, complex):
        return -result.real
    return result

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

    left_bound = 3
    precision = 99

    for whole in range(0, left_bound):
        for num in range(0, precision):
            x = -whole + ((-num) / precision)
            y = f(whole * precision + num, precision)
            plt.plot(x, y, "ro")

    plt.xlim([-left_bound, 0])
    plt.ylim([-2, 2])

    plt.show()
# I spent half an hour on this and I don't think it proves anything
