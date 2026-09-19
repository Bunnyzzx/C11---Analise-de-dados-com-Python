import numpy as np

np.random.seed(10)
mtz = np.random.randint(1, 51, (4,4))

medLmtz = mtz.mean(axis = 1)
medCmtz = mtz.mean(axis = 0)

print(f'media de cada linha: {medLmtz}')
print(f'media de cada coluna: {medCmtz}')
print(f'Maior valor na MED das linhas: {medLmtz.max()}')
print(f'Maior valor na MED das colunas: {medCmtz.max()}')

valores, contagens = np.unique(mtz, return_counts=True)

for valor, quantidade in zip(valores, contagens):
    print(f'{valor}: {quantidade}')

print('numeros que aparecem 2 vezes:')

print(valores[contagens == 2])