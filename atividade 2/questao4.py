dist = int(input("Distancia viagem em km: "))

if dist <= 200:
    valor_km = 0.5

else:
    valor_km = 0.45

valor_total = dist*valor_km
print(f"Valor total: R${valor_total}")