import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

paises=pd.read_csv('paises.csv',sep=None,engine='python')

colunas=['GDP ($ per capita)','Literacy (%)','Infant mortality (per 1000 births)','Phones (per 1000)']

dados=paises[colunas].copy()

for coluna in colunas:
    dados[coluna]=pd.to_numeric(dados[coluna].astype(str).str.replace(',','.'),errors='coerce')

sns.heatmap(dados.corr(),annot=True,cmap='coolwarm')
plt.show()