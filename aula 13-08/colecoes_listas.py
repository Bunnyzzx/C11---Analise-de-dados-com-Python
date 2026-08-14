#listas
nomes  = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print(type(nomes))

#inserction de dados na list
nomes.append('Bulma') #em ultimo na lista
nomes.insert(2,'Kuririn') # posicao especifica, vai empurrando os q estao na frente dele
nomes.insert(2,'Kuririn')
nomes.insert(0,'Picollo') #em primeiro na lista


#removendo da lista
del nomes[4] #apaga da posicao 3

nome_removido = nomes.pop(3) #apaga por indice
print(f"nome removido foi: {nome_removido}")

if 'Gohan' in nomes:
    nomes.remove('Gohan') #apaga a primeira ocorrencia do nome gohan
    print("Removido da lista!")
else:
    print("Nao esta na lista!")

tamanho_lista = len(nomes)

if tamanho_lista > 4:
    nomes.pop(4)
    print("Item removido por indice")
else:
    print("Lista muito pequeno, nao removido")

print(len(nomes)) # print tamanho lista

nomes.sort() #ord crescente
nomes.sort(reverse = True) #ord decrescente

print(nomes)


