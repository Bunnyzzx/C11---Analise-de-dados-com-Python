import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter=';', dtype=str)
dados = dataset[1:]
#engagement = 9

engagement = dados[:,9]
engLow = engagement[engagement =='Low']
pctg = len(engLow) / len(engagement) * 100
print(f'{pctg:.2f} %')