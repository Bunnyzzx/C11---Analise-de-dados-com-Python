nomes_set  = {'Goku', 'Vegeta', 'Trunks', 'Gohan','Trunks'}
#colecoes nao permitem itens iguais, mesmo nome, mesmo valor
print(nomes_set)
print(type(nomes_set))
nomes_set.remove('Trunks')
nomes_set.add('TRUNKS')
print(nomes_set)

print("")
a = {2,6,8}
b = {1,6,5}

#uniao
z = a | b
print(f'Uniao: {z}')

#Diferenca
z1 = a - b
print(f'Diferenca: {z1}')

#Intersecao
z2 = a & b
print(f'Interseção: {z2}')