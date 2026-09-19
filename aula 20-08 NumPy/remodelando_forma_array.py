import numpy as np

arr = np.arange(9)
print(arr)

matriz = arr.reshape([3,3]) #precisa ter o mesmo tamanho da array unideimensional
print(matriz)

print('')
print(f'tamanho array: {matriz.size}')
print(f'qnt dimensoes: {matriz.ndim}')
print(f'qual o corpo, modelo da matriz? {matriz.shape}')
print(f'soma da coluna: {matriz.sum(axis = 0)}')
print(f'soma da linha: {matriz.sum(axis = 1)}')
#axis = linha, coluna, ou altura (x,y,z)
# axix = 0 -> coluna
print(f'operacoes entre matriz e um escalar: ')
print(matriz/5)
print('')
print(matriz*2)
print('')
print(matriz-3)
print('')
