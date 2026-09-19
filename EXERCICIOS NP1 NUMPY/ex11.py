import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype=str)

dados = dataset[1:]

local = dados[:, 2]

condicao = np.char.find(local, 'USA') >= 0

local_usa = local[condicao]

print(local_usa)