import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter=';', dtype=str)
dados = dataset[1:]
#plataforma = 1
#views = 5

plataforma = dados[:, 1]
views = dados[:, 5].astype(int)
maiorview = views.max()
indice = np.argmax(views)


print(f'maior quantidade de views: {maiorview} views')
print(f'referente a plataforma: {plataforma[indice]}')