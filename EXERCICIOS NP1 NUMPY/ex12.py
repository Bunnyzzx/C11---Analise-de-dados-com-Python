import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype=str)

dados = dataset[1:]
empresa = dados[:,1]
spacex = empresa[empresa == 'SpaceX']
custo = dados[:,6].astype(float)

custosSpaceX = custo[empresa == 'SpaceX']
maiorCustoSpaceX = custosSpaceX.max()
print(maiorCustoSpaceX)