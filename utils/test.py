import numpy as np

matrix_size = 11
matrix = np.ones((matrix_size, matrix_size))
for line in range(matrix_size):
    for i in range(matrix_size):
        if line < matrix_size / 2:
            if i <= ((matrix_size - 2 - 2 * line) / 2):
                matrix[line][i] = 0
            if i >= ((matrix_size + 1 + 2 * line) / 2):
                matrix[line][i] = 0
        if line > matrix_size / 2:
            if i <= ((2 * line - matrix_size - 1) / 2):
                matrix[line][i] = 0
            if i >= ((3 * matrix_size - 2 * line - 1) / 2):
                matrix[line][i] = 0
print(matrix)
