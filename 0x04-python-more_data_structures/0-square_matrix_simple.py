#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_n = matrix.copy()
    for i in range(len(matrix_n)):
        matrix_n[i] = matrix[i].copy()
        for j in range(len(matrix_n[i])):
            matrix_n[i][j] **= 2
    return (matrix_n)
