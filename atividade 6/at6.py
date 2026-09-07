import pandas as pd
import numpy as np

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print(seriesAno1)
print(seriesAno2)

print(seriesAno1.sum())
print(seriesAno2.sum())

crescimento = seriesAno2 - seriesAno1

print(crescimento)

print(crescimento[crescimento > 0])

proximosAnos = seriesAno2 + crescimento * 2

print(proximosAnos.nlargest(1))

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

print(df)

media = df[df['X'] < 30]['X'].mean()

print(media)

mediaD = df.loc['D'].mean()

print(mediaD)

somaE = df.iloc[4].sum()

print(somaE)

recorte = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print(recorte)

print(recorte.sum(axis=1))

print(recorte.sum(axis=0))