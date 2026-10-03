import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", delimiter=";")

sucesso = df[df["Status Mission"] == "Success"]
falha = df[df["Status Mission"] == "Failure"]

topSucesso = sucesso["Company Name"].value_counts().head(5)
topFalha = falha["Company Name"].value_counts().head(5)

plt.subplot(1, 2, 1)
plt.bar(topSucesso.index, topSucesso.values)
plt.title("Top 5 - Success")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.bar(topFalha.index, topFalha.values)
plt.title("Top 5 - Failure")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()