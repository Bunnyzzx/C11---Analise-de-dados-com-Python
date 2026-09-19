import pandas as pd

df = pd.read_csv("paises.csv")

# questao 1
oceania = df[df["Region"].str.contains("OCEANIA")]

print(oceania["Country"])
print("quantidade:", len(oceania))


# questao 2
maior = df["Population"].idxmax()

print("pais:", df.loc[maior, "Country"])
print("regiao:", df.loc[maior, "Region"])


# questao 3
df["Literacy (%)"] = df["Literacy (%)"].str.replace(",", ".").astype(float)

media = df.groupby("Region")["Literacy (%)"].mean()

print(media)


# questao 4
df["Coastline (coast/area ratio)"] = df["Coastline (coast/area ratio)"].str.replace(",", ".").astype(float)

sem_costa = df[df["Coastline (coast/area ratio)"] == 0]

print(sem_costa["Country"])

sem_costa.to_csv("noCoast.csv", index=False)


# questao 5
df["Deathrate"] = df["Deathrate"].str.replace(",", ".").astype(float)

def ajuda(valor):
    if valor <= 9:
        return "Balanced"
    else:
        return "Urgent"

df["Humanitarian Help"] = df["Deathrate"].apply(ajuda)

print(df)