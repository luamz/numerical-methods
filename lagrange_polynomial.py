# Example function and points
def f(x):
    return x - (2/x)


p_x = [1,    2,    2.5]
p_y = [f(1), f(2), f(2.5)]

# Finds respective L0/L1/L2 for x


def L(x, n, xi, i, p_x):
    result = 1
    for j in range(n):
        xj = p_x[j]
        if i != j:
            result *= (x - xj) / (xi - xj)
    return result

# Solves polynomial


def P(x, n, p_x, p_y):
    result = 0
    for i in range(n):
        yi = p_y[i]
        xi = p_x[i]
        result += yi * L(x, n, xi, i, p_x)
    return result


# Execution
print("----- Lagrange polynomial -----\n")

print("Example:\nf(x) = x - (2/x)\nWith x0 =",
      p_x[0], ", x1 =", p_x[1], ", x2 =", p_x[2])
print("Applied at (1,2) e (2,2)\n")

print("P(1.2) = %.5f" % P(1.2, 3, p_x, p_y))
print("P(2.2) = %.5f" % P(2.2, 3, p_x, p_y))
