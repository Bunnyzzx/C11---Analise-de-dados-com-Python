import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))

print("Matriz:")
print(matriz)

# A
mediaLinhas = matriz.mean(axis=1)
mediaColunas = matriz.mean(axis=0)

print("media de cada linha:")
print(mediaLinhas)

print("media de cada coluna:")
print(mediaColunas)

# B
print("maior média das linhas:")
print(mediaLinhas.max())

print("maior média das colunas:")
print(mediaColunas.max())

# C
numeros, quantidades = np.unique(matriz, return_counts=True)

print("qnt de aparições:")
for i in range(len(numeros)):
    print(f"{numeros[i]} aparece {quantidades[i]} vez(es)")

print("numeros que aparecem 2 vezes:")
print(numeros[quantidades == 2])