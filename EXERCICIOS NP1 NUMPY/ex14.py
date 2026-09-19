import numpy as np
dataset = np.loadtxt('space.csv',delimiter= ';',dtype= str, encoding='utf-8')
header = dataset[0]
dados = dataset[1:]
print(header)

missoes = dados[:,7]
sucesso = missoes[missoes == 'Success']
pctg = len(sucesso) / len(missoes) * 100
print(f'{pctg:.2f}% de sucesso')