def aplicar

while True:
    gen = input("Digite seu genero: (M-Homem) (F=Mulher)")

    if gen == "M" or gen == "m":
        print("Homem")
        break
    
    elif gen == "F" or gen == "f":
        print("Mulher")
        break
    
    else:
        print("Opcao invalida!")