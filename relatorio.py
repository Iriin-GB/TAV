from functions import *
from random import randint
from collections import Counter
import csv

QNTJGDS = 100000

# Função para escolher o modo de jogo
def escolherModo():
    print("Escolha o modo de jogo:")
    print("1. Campeão vs Aleatório")
    print("2. Aleatório vs Aleatório")
    print("3. Campeão vs Campeão")  # Nova opção para Campeão vs Campeão
    modo = int(input("Digite o número do modo que deseja jogar: "))
    return modo

# Função para escolher quem será o primeiro a jogar
def escolherQuemComeca():
    print("Escolha quem será o primeiro a jogar:")
    print("1. X (Jogador 1)")
    print("2. O (Jogador 2)")
    print("3. Aleatório")
    escolha = int(input("Digite o número da sua escolha: "))
    if escolha == 1:
        return 1  # X começa
    elif escolha == 2:
        return 2  # O começa
    else:
        return randint(1, 2)  # Aleatório

# Inicializa o modo de jogo
modo_de_jogo = escolherModo()
jogador_inicial = escolherQuemComeca()  # Escolhe uma única vez quem começa

resultados = []  # Lista para armazenar o vencedor de cada jogo
dados_jogos = []  # Lista para armazenar dados de cada jogo (número de rodadas e jogadas)
printe = 0
media_jogadas = 0  # Para calcular a média de jogadas ao longo dos jogos
vitorias_o = 0
vitorias_x = 0
empates = 0

# Abre o arquivo CSV para salvar os dados
with open('resultados_jogos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Jogo", "Quem Começou", "Rodadas", "Jogadas", "Resultado", "Média de Jogadas Até o Momento", "Porcentagem X", "Porcentagem O", "Porcentagem Velha"])

    for i in range(QNTJGDS):  # Executa QNTJGDS partidas
        # Reinicializa o jogo para cada iteração
        jogo[0] = 0  # Número de jogadas
        for pos in range(1, 10):
            jogo[pos] = '_' if pos <= 6 else ' '  # Reinicializa o tabuleiro

        jogador = jogador_inicial  # Usa a escolha inicial
        jogadas = []  # Armazena a ordem de jogadas
        rodadas = 0  # Conta o número de rodadas

        while jogo[0] < 9:
            rodadas += 1
            
            if jogador == 1:  # Jogador X joga
                if modo_de_jogo == 1 or modo_de_jogo == 3:  # Campeão joga em ambos os modos
                    escolha = jogadaCampeao()  # Jogador X (campeão)
                else:
                    escolha = jogadaAleat()  # Jogador X (aleatório)
                jogadas.append(f"X-{escolha}")  # Armazena a jogada de X
                escolha = verificarPosicao(escolha, 1)  # Verifica a jogada do jogador X
                jogador = 2  # Alterna para o jogador O
                
            else:  # Jogador O joga
                if modo_de_jogo == 3:  # Campeão joga em Campeão vs Campeão
                    escolha = jogadaCampeao()  # Jogador O (campeão)
                else:
                    escolha = jogadaAleat()  # Jogador O (aleatório)
                jogadas.append(f"O-{escolha}")  # Armazena a jogada de O
                escolha = verificarPosicao(escolha, 2)  # Verifica a jogada do jogador O
                jogador = 1  # Alterna para o jogador X
            
            # Verifica o status do jogo
            status = verificaJogo()

            # Se algum jogador vencer, registra o resultado e encerra a partida
            if status == 1:  # Jogador X venceu
                resultado = "X"
                vitorias_x += 1
                resultados.append(resultado)
                dados_jogos.append((rodadas, jogadas))  # Armazena dados do jogo
                break
            elif status == 2:  # Jogador O venceu
                resultado = "O"
                vitorias_o += 1
                resultados.append(resultado)
                dados_jogos.append((rodadas, jogadas))  # Armazena dados do jogo
                break
            elif status == 0 and jogo[0] == 9:  # Empate (Velha)
                resultado = "Velha"
                empates += 1
                resultados.append(resultado)
                dados_jogos.append((rodadas, jogadas))  # Armazena dados do jogo
                break

        # Atualiza a média de jogadas
        media_jogadas = ((media_jogadas * i) + rodadas) / (i + 1)

        # Calcula as porcentagens acumuladas
        porcentagem_x = (vitorias_x / (i + 1)) * 100
        porcentagem_o = (vitorias_o / (i + 1)) * 100
        porcentagem_empate = (empates / (i + 1)) * 100

        # Determina quem começou o jogo
        quem_comecou = "X" if jogador_inicial == 1 else "O"

        # Salva os dados no CSV, incluindo quem começou
        writer.writerow([i+1, quem_comecou, rodadas, ";".join(jogadas), resultado, f"{media_jogadas:.2f}", f"{porcentagem_x:.2f}%", f"{porcentagem_o:.2f}%", f"{porcentagem_empate:.2f}%"])

        printe += 1
        print(f'Foi a rodada: {printe}')  # Mantém o controle das rodadas

# Exibe uma mensagem confirmando a geração do arquivo CSV
print("\nArquivo 'resultados_jogos.csv' gerado com sucesso!")

# Exibe os resultados finais
probabilidade_o = (vitorias_o / QNTJGDS) * 100  # Probabilidade de vitória de O
probabilidade_x = (vitorias_x / QNTJGDS) * 100  # Probabilidade de vitória de X
probabilidade_empate = (empates / QNTJGDS) * 100  # Probabilidade de empate

# Exibe os resultados finais
print(f"\nResultados após {QNTJGDS} jogos:")
print(f"Jogador X venceu {vitorias_x} vezes ({probabilidade_x:.2f}%).")
print(f"Jogador O venceu {vitorias_o} vezes ({probabilidade_o:.2f}%).")
print(f"Empates (Velha): {empates} vezes ({probabilidade_empate:.2f}%).")

# Contabiliza a frequência dos resultados
resultado_counter = Counter(resultados)
mais_comuns = resultado_counter.most_common(10)  # Obtém os 10 resultados mais comuns

# Exibe os resultados mais comuns
# print("\n10 Resultados Mais Ocorridos:")
# for resultado, contagem in mais_comuns:
#     print(f"{resultado}: {contagem} vezes")
