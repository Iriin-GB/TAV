from random import randint

jogo = [0, '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', 0]

def gerarTabuleiro():
    tabuleiroJogadores = {1: 'X', 2: 'O', '_': '_', ' ': ' '}
    global jogo

    print('_' + tabuleiroJogadores[jogo[1]] + '_|_' + tabuleiroJogadores[jogo[2]] + '_|_' + tabuleiroJogadores[jogo[3]] + '_')
    print('_' + tabuleiroJogadores[jogo[4]] + '_|_' + tabuleiroJogadores[jogo[5]] + '_|_' + tabuleiroJogadores[jogo[6]] + '_')
    print(' ' + tabuleiroJogadores[jogo[7]] + ' | ' + tabuleiroJogadores[jogo[8]] + ' | ' + tabuleiroJogadores[jogo[9]])

def verificarPosicao(escolha, jogador):
    global jogo
    escolhaArray = escolha

    if jogo[escolhaArray] == '_' or jogo[escolhaArray] == ' ':
        jogo[escolhaArray] = jogador
        jogo[0] += 1
        return 2 if jogador == 1 else 1  # Alterna o jogador
    else:
        print('Posição inválida, selecione uma casa ainda não jogada!')
        return jogador

def verificaJogo():
    vitorias = [
        (1, 2, 3),  # linha 1
        (4, 5, 6),  # linha 2
        (7, 8, 9),  # linha 3
        (1, 4, 7),  # coluna 1
        (2, 5, 8),  # coluna 2
        (3, 6, 9),  # coluna 3
        (1, 5, 9),  # diagonal 1
        (3, 5, 7)   # diagonal 2
    ]
        
    for a, b, c in vitorias:
        if jogo[a] == jogo[b] == jogo[c] and type(jogo[a]) == type(1):
            jogo[10] = jogo[a]
            # print ('Resultado é '+ str(jogo[10]))
            return jogo[10]
    
    return 0  # Retorna 0 se não houver vencedor

def quemComeca():
    aleat = randint(1, 2)
    print("Quem começa é o " + str(aleat) + "!\n")
    return aleat

def jogadaAleat():
    global jogo
    while True:
        jogadaAleatBot = randint(1, 9)
        if jogo[jogadaAleatBot] == '_' or jogo[jogadaAleatBot] == ' ':
            return jogadaAleatBot  # Retorna uma jogada válida

def jogadaCampeao():
    global jogo
    # 1. Ganhar se possível
    for a, b, c in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]:
        if jogo[a] == jogo[b] == 1 and jogo[c] in ['_', ' ']:  # Bloqueia 'X' (1)
            return c
        if jogo[a] == jogo[c] == 1 and jogo[b] in ['_', ' ']:
            return b
        if jogo[b] == jogo[c] == 1 and jogo[a] in ['_', ' ']:
            return a

    # 2.1 Prioridade: Bloquear o oponente (2) nas colunas verticais
    for a, b, c in [(1, 4, 7), (2, 5, 8), (3, 6, 9)]:
        if jogo[a] == jogo[b] == 2 and jogo[c] in ['_', ' ']:
            return c
        if jogo[a] == jogo[c] == 2 and jogo[b] in ['_', ' ']:
            return b
        if jogo[b] == jogo[c] == 2 and jogo[a] in ['_', ' ']:
            return a

    # 2.2 Bloquear o oponente (2) nas outras direções
    for a, b, c in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7)]:
        if jogo[a] == jogo[b] == 2 and jogo[c] in ['_', ' ']:
            return c
        if jogo[a] == jogo[c] == 2 and jogo[b] in ['_', ' ']:
            return b
        if jogo[b] == jogo[c] == 2 and jogo[a] in ['_', ' ']:
            return a

    # 3. Verifica e bloqueia padrões perigosos de "O" (cantos opostos)
    if (jogo[1] == 2 and jogo[9] == 2) or (jogo[3] == 2 and jogo[7] == 2):
        for pos in [2, 4, 6, 8]:  # Prioriza lados para bloquear o padrão de cantos
            if jogo[pos] in ['_', ' ']:
                return pos

     # 4. Bloqueia padrões de jogadas específicas que resultaram em vitórias de 'O'
    perigosas = [
        (7, 6, 9), (8, 6, 9), (1, 8, 7), (8, 3, 7), (3, 8, 7), (6, 5, 9)
    ]

    for a, b, c in perigosas:
        if jogo[a] == 2 and jogo[b] == 2 and jogo[c] in ['_', ' ']:  # Bloqueia padrões perigosos
            return c

    # 5. Joga no centro se possível
    if jogo[5] in ['_', ' ']:
        return 5

    # 6. Bloqueia o padrão de controle de cantos opostos
    for a, b, c in [(1, 3, 2), (7, 9, 8), (1, 7, 4), (3, 9, 6)]:
        if jogo[a] == 2 and jogo[c] == 2 and jogo[b] in ['_', ' ']:  # Bloqueia cantos consecutivos
            return b

    # 7. Joga em um dos cantos
    for pos in [1, 3, 7, 9]:
        if jogo[pos] in ['_', ' ']:
            return pos

    # 8. Joga nos lados
    for pos in [2, 4, 6, 8]:
        if jogo[pos] in ['_', ' ']:
            return pos

    print(f'o tabuleiro e  {jogo}')