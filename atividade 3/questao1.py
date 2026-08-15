times = ["Cruzeiro", "Barcelona", 'Flamengo', 'Real Madrid', 'Palmeiras']

top3 = times[:3]
print(f'Top 3:')
print(top3)

print('')

top2piores = times[-2:]
print(f'Os 2 piores times:')
print(top2piores)

print('')


timesSorteados = sorted(times)
print('Ordem alfabetica')
print(timesSorteados)

print('')


posicao = times.index('Barcelona')
print (f'posicao do barcelona: ' [posicao])
