import numpy as np

arr = np.arange(10, 31, 2)

print("Array:")
print(arr)

print("Maior valor:", arr.max())
print("Índice do maior valor:", arr.argmax())

print("Menor valor:", arr.min())
print("Índice do menor valor:", arr.argmin())

print("Soma dos elementos:", arr.sum())