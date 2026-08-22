import numpy as np
confirmacao = True
jogadas = 0
arr = np.zeros((2,2))
posJogadas = []

linhaAleatoria = np.random.randint(0, 2)
colunaAleatoria = np.random.randint(0, 2)
arr[linhaAleatoria, colunaAleatoria] = 1

while(confirmacao == True ) and (jogadas<3):
    print('')
    posLinha = int(input("Digite a linha em que deseja jogar(0 ou 1): "))
    posColuna = int(input("Digite a coluna em que deseja jogar(0 ou 1): "))

    if (posLinha, posColuna) in posJogadas:
        print("Você já jogou nessa posição!")
        continue
    
    posJogadas.append((posLinha, posColuna))
    
    print('')
    if arr[posLinha,posColuna] == 1:
        print('')
        print('perdeu playboy kkkk fim de jogo!')
        confirmacao = False
    else:
        jogadas += 1
        print(f'boa, tem que acertar mais {3-jogadas} vezes!')

    if jogadas == 3:
        print('parabens campeao, ganho o game')

    


