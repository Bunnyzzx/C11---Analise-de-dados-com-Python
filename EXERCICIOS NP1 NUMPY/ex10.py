import numpy as np
dataset = np.loadtxt('space.csv',delimiter=';',dtype=str)
dados = dataset[1:]
header = dataset[0]
custo = dados[:,6].astype(float)
custovalido = custo[custo > 0]
medgasto = sum(custovalido)/len(custovalido)

print(f'{medgasto:.2f}')

