import numpy as np
import random

matrix_size = 3

matrix_1 = [[0] * matrix_size for _ in range(matrix_size)]
matrix_2 = [[0] * matrix_size for _ in range(matrix_size)]
result = [[0] * matrix_size for _ in range(matrix_size)]

# Creamos las matrices de forma aleatoria

for i in range(matrix_size):
    for j in range(matrix_size):
        matrix_1[i][j] = random.randint(-5, 5)
        matrix_2[i][j] = random.randint(-5, 5)

# Realizamos la multiplicación

for i in range(matrix_size):
    for j in range(matrix_size):
        for e in range(matrix_size):
            result[i, j] = matrix_1[i][j]

