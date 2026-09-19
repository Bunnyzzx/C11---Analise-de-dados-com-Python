import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str, encoding='utf-8')
header = dataset[0]
dados = dataset[1 :]

print(header)

custo = dados[: , 6].astype(float)
custoValido = custo[custo > 0]

med = sum(custoValido)/len(custoValido)
print(f'custo medio de: {med:.2f}$')