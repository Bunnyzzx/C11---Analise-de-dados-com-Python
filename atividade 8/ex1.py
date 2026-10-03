import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("paises.csv", delimiter=";")

americaNorte = df[df["Region"].str.strip() == "NORTHERN AMERICA"]

x = americaNorte["Country"]
deathrate = americaNorte["Deathrate"]
birthrate = americaNorte["Birthrate"]

plt.plot(x, deathrate, "r-", label="Deathrate")
plt.plot(x, birthrate, "b-", label="Birthrate")

plt.xlabel("Paises")
plt.ylabel("Taxa")
plt.title("Natalidade e Mortalidade - America do Norte")

plt.legend()
plt.show()