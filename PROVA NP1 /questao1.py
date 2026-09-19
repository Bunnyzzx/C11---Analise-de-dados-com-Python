import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter=';', dtype=str)
dados = dataset[1:]
tipo = dados[:,3]
video = tipo[tipo == 'Video']
qntVideos = len(video)
print(f'quantidade de posts que possuem o Content_Type "Video": {qntVideos}')