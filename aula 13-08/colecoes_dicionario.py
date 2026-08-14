dados = {
    "nome" : "goku",
    "idade" : 47,
    "temNome" : True
}

dados1 = {
    "nome" : "gohan",
    "idade" : 22,
    "temNome" : True
}

dados2 = {
    "nome" : "vegeta",
    "idade" : 50,
    "temNome" : True
}

print(dados)
print(dados['nome'])

dados['sexo'] = 'M'
print(dados)

del dados['sexo']
dados['idade'] = 40
print(dados)


banco = []
banco.append(dados)
banco.append(dados1)
banco.append(dados2)

for dicts in banco:
    print(dicts)