import numpy as np

arr = np.zeros((3, 4))

linhas, colunas = arr.shape

total = linhas * colunas

if total % 2 == 0:
    print("A matriz pode se tornar um vetor unidimensional com número par de elementos.")
else:
    print("A matriz pode se tornar um vetor unidimensional com número ímpar de elementos.")