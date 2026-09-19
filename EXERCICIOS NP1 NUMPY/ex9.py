import numpy as np
dataset = np.loadtxt('space.csv',delimiter=';',dtype=str)
header = dataset[0]
dados = dataset[1:]
status = dataset[: , 7]
sucesso = status[status == 'Success']

porcentagem = len(sucesso) / len(status) * 100
print(porcentagem)
