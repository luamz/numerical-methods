import math

# Checks if Gauss-Seidel method is applicable
def ValidatesMatrix(A):
    coefficient = []
    for i in range(len(A)):
        b = 0
        for j in range(len(A)):
            if (i != j and i == 0) or i < j:
                b += A[i][j]
            elif i != j and i != 0:
                b += A[i][j]*coefficient[j]
        b /= A[i][i]
        coefficient.append(b)
    if max(coefficient) > 1:
        print('Gauss-Seidel method is not applicable!')
        return 0
    else:
        return 1

# Finds the highest difference between current and previous solution


def difference(previous, current):
    difference = []
    for i in range(len(previous)):
        Diff = abs(current[i] - previous[i])
        difference.append(Diff)
    return max(difference)


def GaussSeidel(A, B, current_solutions, number_of_iterations, error):
    if ValidatesMatrix(A):
        for i in range(number_of_iterations):
            previous = []
            for xn in current_solutions:
                previous.append(xn)

            for j in range(len(A)):
                x = B[j]
                for k in range(len(A)):
                    if j != k:
                        x -= A[j][k]*current_solutions[k]
                x /= A[j][j]
                current_solutions[j] = x

            print("Iteration", i+1, "-", end="")
            resp = ""
            for solution in current_solutions:
                resp += ' ' + str(solution)
            print(resp)

            # Checks if difference has reached acceptable precision
            if difference(previous, current_solutions) < error:
                print("Max precision reached!")
                break


# Example
A = [
    [12, 3, -5],
    [1, 5,  3],
    [3, 7, 13]
]
B = [1, 28, 76]

initial_guess = [1, 0, 1]
number_of_iterations = 20
error = 0.00000001

# Execution
print("----- Gauss-Seidel Method-----")
GaussSeidel(A, B, initial_guess, number_of_iterations, error)
