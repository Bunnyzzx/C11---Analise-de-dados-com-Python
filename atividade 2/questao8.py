x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))

adicao = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y
resto = x % y
potencia = x ** y

print(f"Adicao: {adicao}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Divisao: {divisao}")
print(f"Resto da divisao: {resto}")
print(f"Potencia: {potencia}")

if adicao % 2 == 0:
    print("O resultado da adicao e par.")
else:
    print("O resultado da adicao e impar.")