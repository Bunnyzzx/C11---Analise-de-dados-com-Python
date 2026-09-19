import numpy as np

np.random.seed(10)

mtz = np.random.randint(1,51, (4,4))

medLmtz = mtz.mean(axis = 1)
medCmtz = mtz.mean(axis = 0)
print(f'media de cada linha: {medLmtz}')
print('')
print(f'media de cada coluna: {medCmtz}')
print('')
maiorL = medLmtz.max()
maiorC = medCmtz.max()
print(f'maior valor da coluna med {maiorC}')
print('')
print(f'maior valor da linha med {maiorL}')


valores, contagem = np.unique(mtz, return_counts= True)
for valor, quantidade in zip(valores, contagem):
    print(f'{valor} : {quantidade}')
print(valores[contagem == 2])