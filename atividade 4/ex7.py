import numpy as np

np.random.seed(7)

arr1 = np.random.randint(1, 11, 5)
arr2 = np.random.randint(1, 11, 5)

arr3 = np.concatenate((arr1, arr2))

matriz = arr3.reshape(2, 5)

print("Primeiro array:")
print(arr1)

print("\nSegundo array:")
print(arr2)

print("\nArrays concatenados:")
print(arr3)

print("\nMatriz 2x5:")
print(matriz)