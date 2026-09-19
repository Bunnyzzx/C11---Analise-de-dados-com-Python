import numpy as np 
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str)

dados = dataset[1:]
empresas = dados[:,1]

empresas_unicas, quantidade = np.unique(empresas, return_counts=True)

for empresa, qtd in zip(empresas_unicas, quantidade):
    print(empresa, qtd)

