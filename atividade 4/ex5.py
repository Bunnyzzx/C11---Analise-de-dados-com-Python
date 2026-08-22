import numpy as np

matrizZeros = np.zeros((3, 3))
matrizUns = np.ones((3, 3))

soma = matrizZeros + matrizUns

escalar = 5
resultado = soma * escalar

vetor = resultado.reshape(9)

print("Matriz de zeros:")
print(matrizZeros)

print("\nMatriz de uns:")
print(matrizUns)

print("\nSoma:")
print(soma)

print("\nMultiplicada pelo escalar:")
print(resultado)

print("\nArray unidimensional:")
print(vetor)