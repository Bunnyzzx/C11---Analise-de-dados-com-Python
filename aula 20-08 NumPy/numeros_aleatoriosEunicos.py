import numpy as np

np.random.seed(5)
arr = np.random.randint(0,10,10)
print(arr)
print('')

matriz = np.random.randint(0,10,[5,5])
print(matriz)
print('')

#identifica numeros unicos e contabiliza a recorrencia de repeticoes
arr = np.array([1,2,3,4,5,2,3,4])
print(np.unique(arr))
print(np.unique(arr, return_counts = True))