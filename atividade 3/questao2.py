loja1 = {'Iphone 14','Iphone 14 Pro','Iphone 14 Pro Max','Iphone 16', 'Asusphone 7'}
loja2 = {'Samsung A50', 'Samsung S20', 'Asusphone 7', 'Iphone 14'}

print(f'opcoes loja 1:')
print(loja1)
print('')
print(f'opcoes loja 2:')
print(loja2)
print('')

todasOpcoes = loja1 | loja2
total = len(todasOpcoes)
print(f'todas opcoes disponiveis em ambas: {todasOpcoes}')
print(f'quantidade: {total}')
print('')

apenasLj1 = loja1-loja2
print(f'opcoes exclusivas lj1: {apenasLj1}')
print('')

apenasLj2 = loja2-loja1
print(f'opcoes exclusivas lj2: {apenasLj2}')
print('')