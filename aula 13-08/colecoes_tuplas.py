#Tuplas

nomes_tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes_tupla)
print(type(nomes_tupla))

#tupla eh imutavel, entao nao eh possivel alterar oq for adicionado nela

for nome in nomes_tupla:
    print(nome)

print('')


for count in range(len(nomes_tupla)):
    print(f"Indice: {count}, Valor: {nomes_tupla[count]}")
print('')
print('')
print('')

#operacoes com tupla
a = (2, 6, 8)
b = (4, 6, 9, 5)
z = a + b

print(z)
print(min(z), max(z))
print(z.count(6)) #qnt repeticoes mesmo valor
print(z.index(9)) #valor de uma tupla