import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(f'valor minimo: {arr.min()}, indice: {arr.argmin()}')
print(f'valor max: {arr.max()}, indice: {arr.argmax()}')
print(f'Foma: {arr.sum()}, media: {arr.mean()}')
print(arr)
print("")
print(f'soma indice a indice: {arr+arr2}')
print(f'multiplicacao indice a indice: {arr*arr2}')
print(f'juntar 2 arrays: {np.concatenate((arr,arr2))}')
