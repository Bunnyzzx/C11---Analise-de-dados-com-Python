import numpy as np

arr0 = np.zeros([2,2])
#posicoes
#00 - 01
#10 - 11

x = np.random.randint(0,2)
y = np.random.randint(0,2)
arrxy = [x,y]
arr0[x,y] = 1
print(arr0)

jogadas = 3
condicao = True
while condicao == True:
    print(f'Voce ainda tem {jogadas} jogadas disponiveis')
    l = int(input('Digite a linha: '))
    c = int(input('Digite a coluna: '))
    print('')

    if arr0[l,c] == 1:
        print('Game Over! :( Try Again!')
        condicao = False
        break

    elif arr0[l,c] == 0:
        arr0[l,c] = -1
        jogadas = jogadas - 1
        print(f'boa jogada!')
        print('')

    elif arr0[l,c] == -1:
        print('Posicao já escolhida!')
        print('')

    if jogadas == 0:
        print('Congratulations! You beat the game! :)')
        condicao = False
        break

