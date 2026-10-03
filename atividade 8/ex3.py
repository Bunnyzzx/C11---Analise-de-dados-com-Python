import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", delimiter=";")

roscosmos = df[df["Company Name"] == "Roscosmos"]

status = roscosmos["Status Mission"].value_counts()

plt.pie(status.values, labels=status.index, autopct="%1.1f%%")

plt.title("Missoes da Roscosmos")

plt.show()