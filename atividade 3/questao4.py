nomes = []
pesos = []

for i in range(3):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
    peso = float(input(f"Digite o peso {i+1}: "))
    pesos.append(peso)

pos_mais_pesada = pesos.index(max(pesos))
pos_mais_leve = pesos.index(min(pesos))

print(f"A pessoa mais pesada é {nomes[pos_mais_pesada]}, com {pesos[pos_mais_pesada]} kg")
print(f"A pessoa mais leve é {nomes[pos_mais_leve]}, com {pesos[pos_mais_leve]} kg")