# Tommy D. Michailidis
# 2023-12-06
# Final Exam

import random


def matrix_multiply(m1, m2, n):
    result = []
    count = 0
    for r in range(n):
        new_row = []
        for c in range(n):
            new_row.append(0)
            for i in range(n):
                new_row[c] += m1[r][i] * m2[i][c]
                count += 1
        result.append(new_row)
    return count, result


def generate_n_by_n_matrix(n):
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(r * n + c)
        result.append(row)
    return result


for n in range(20, 201, 20):
    matrix1 = generate_n_by_n_matrix(n)  # generate an nxn matrix (matrix1)
    matrix2 = generate_n_by_n_matrix(n)  # generate an nxn matrix (matrix2)
    count, result = matrix_multiply(matrix1, matrix2, n)  # multiply the two matrices
    print(f"{n:03d} {count // 100000 * '*'}")

# The big-oh notation for this function is O(n^3)
