x = int(input("Digite um valor entre 1000 e 9999: "))

unidade = x % 10
dezena = (x // 10) % 10
centena = (x // 100) % 10
milhar = (x // 1000) % 10

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
