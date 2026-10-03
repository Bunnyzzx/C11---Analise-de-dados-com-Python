import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", delimiter=";")

falhas = df[df["Status Mission"] == "Failure"]

topFalhas = falhas["Company Name"].value_counts().head(5)

plt.bar(topFalhas.index, topFalhas.values, color="red")

plt.xlabel("Empresas")
plt.ylabel("Quantidade de falhas")
plt.title("Empresas com mais missoes Failure")

plt.xticks(rotation=45)

plt.show()