palavra = input("Digite a palavra: ")
vogais = 0
for letra in palavra:
    print(letra.upper())

    if letra.lower() == a or letra.lower() == e or letra.lower() == i or letra.lower() == o or letra.lower() == u
        vogais += 1
    
print(f"A palavra possui {vogais} vogais.")

if "a" in palavra.lower():
    print("A letra 'a' esta presente na palavra.")
else:
    print("A letra 'a' nao esta presente na palavra.")
