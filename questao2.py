x = int(input("Digite um valor para calcular a tabuada: "))
y = int(input("Digite ate onde deve ser calculada a tabuada: "))
i = 0

while i != y:
    i += 1
    result = x*i
    print(f"{x} * {i} = {result}")
