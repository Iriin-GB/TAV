from functions import *
from time import sleep

print('Bem vindo ao Jogo da Velha\n')

jogador = quemComeca()

print("O (primeiro) Jogador será o X, Computador/Segundo Jogador O\n\n")

modo = int(input('Qual modo de jogo você gostaria de jogar? \n 1 - Jogador Vs Jogador \n 2 - Jogador Vs Aleatório \n 3 - Aleatório Vs Aleatório \n 4 - Jogador Vs Campeão \n 5 - Aleatório Vs Campeão \n 6 - Campeão Vs Campeão \n'))

while jogo[0] < 9:
    match modo:
        case 1:  # jogador vs jogador
            gerarTabuleiro()
            escolha = int(input('Em qual posição você quer jogar? [1 a 9]:\n'))
            if escolha <= 0 or escolha > 9:
                print('Valor de casa inválida, jogue de novo!')
            else:
                jogador = verificarPosicao(escolha, jogador)

        case 2:  # jogador vs máquina
            if jogador == 1:
                escolha = int(input('Em qual posição você quer jogar? [1 a 9]\n')) 
                if escolha <= 0 or escolha > 9:
                    print('Valor de casa inválida, jogue de novo!')
                else:
                    jogador = verificarPosicao(escolha, jogador) 
            else:
                escolha = jogadaAleat()
                escolha = verificarPosicao(escolha, 2)  # O computador joga
                jogador = 1  # Alterna de volta para o jogador humano
                
        case 3:  # máquina vs máquina
            if jogador == 1:
                # sleep(0.5)
                escolha = jogadaAleat()
                escolha = verificarPosicao(escolha, 1)  
                jogador = 2  
            else:
                # sleep(0.5)
                escolha = jogadaAleat()
                escolha = verificarPosicao(escolha, 2)  
                jogador = 1  

        case 4:  # jogador vs campeão
            gerarTabuleiro()
            if jogador == 1:
                escolha = int(input('Em qual posição você quer jogar? [1 a 9]\n'))  
                if escolha <= 0 or escolha > 9:
                    print('Valor de casa inválida, jogue de novo!')
                else:
                    jogador = verificarPosicao(escolha, jogador)
            else:
                escolha = jogadaCampeao()  # O bot campeão faz sua jogada estratégica
                jogador = verificarPosicao(escolha, 2)
                jogador = 1

        case 5:  # máquina vs campeão
            if jogador == 1:
                # sleep(0.5)
                escolha = jogadaAleat()
                escolha = verificarPosicao(escolha, 1)  
                jogador = 2  
            else:
                # sleep(0.5)
                escolha = jogadaCampeao()
                escolha = verificarPosicao(escolha, 2)  
                jogador = 1     

        case 6:  # campeão vs campeão
            if jogador == 1:
                # sleep(0.5)
                escolha = jogadaCampeao()
                escolha = verificarPosicao(escolha, 1)  
                jogador = 2  
            else:
                # sleep(0.5)
                escolha = jogadaCampeao()
                escolha = verificarPosicao(escolha, 2)  
                jogador = 1     

    status = verificaJogo()

    # Jogador X ganhou (modo jogador vs jogador, jogador vs máquina, jogador vs campeão)
    if status == 1 and modo in [1, 2, 4]:
        print('Jogador X ganhou')
        break

    # Jogador O (bot ou máquina) ganhou
    elif status == 2:
        if modo == 1:
            print('Jogador O ganhou')
        elif modo == 2:
            print('Jogador O (aleatório) ganhou')
        elif modo == 3:
            print('Jogador O (aleatório) ganhou')
        elif modo == 4:
            print('Jogador O (campeão) ganhou')
        elif modo == 5:
            print('Jogador O (campeão) ganhou')
        elif modo == 6:
            print('Jogador O (campeão) ganhou')
        break

    # Jogador X (aleatório) ganhou (modo máquina vs máquina)
    elif status == 1 and modo == 3:
        print('Jogador X (aleatório) ganhou')
        break

    # Empate ("Velha")
    elif status == 0 and jogo[0] == 9:
        print('Velha')
        break
