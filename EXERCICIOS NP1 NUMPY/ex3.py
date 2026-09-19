import numpy as np

linhas = np.random.randint(1, 6)
colunas = np.random.randint(1, 6)
mtz = np.random.randint(0, 10, (linhas, colunas))
print(mtz)
formato = mtz.shape
l = formato[0]
c = formato[1]
m = l*c

if m % 2 == 0:
    print('Poderia ser um array unidimensional par')

else:
    print('Poderia ser um array unidimensional impar')
