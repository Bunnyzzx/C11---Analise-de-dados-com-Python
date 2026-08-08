nome = input("Digite seu nome: ")

print(nome)
print(nome.upper())
print(len(nome.replace(" ","")))
partes = nome.split()
partes[-1] = "Do Inatel"
new_nome = " ".join(partes)
print(new_nome)