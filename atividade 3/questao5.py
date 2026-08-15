n = int(input("Quantas pessoas serao analisadas: "))

pessoas = []

for i in range(n):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ")
    pessoas.append((nome, idade, sexo))

soma_idades = 0
mulheres_menos_20 = 0

for nome, idade, sexo in pessoas:
    soma_idades += idade
    if sexo.upper() == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / n

print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")