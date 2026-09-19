import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter=';', dtype=str)
dados = dataset[1:]
# regiao = 4

regiao = dados[:, 4]
regioes, quantidade = np.unique(regiao, return_counts=True)
indice = np.argmax(quantidade)

print(regioes[indice])
print(quantidade[indice])