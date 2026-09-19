import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter=';', dtype=str)
dados = dataset[1:]
#platforma = 1
#shares = 7
#comments = 8

plataforma = dados[:, 1]
shares = dados[:, 7].astype(int)
comments = dados[:, 8].astype(int)

sharesTikTok = shares[plataforma == 'TikTok']
commentsTikTok = comments[plataforma == 'TikTok']

totShares = sum(sharesTikTok)
totComments = sum(commentsTikTok)

resultado = {
    'shares': totShares,
    'comments': totComments
}

print(resultado)