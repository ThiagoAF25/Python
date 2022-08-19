'''*
Entrega do Trabalho Jogo da Velha- Algoritmos e Programação II
Nós,

Leonardo Pinheiro de Souza
Thiago Aidar Figueiredo


*/'''

def initialize():
    print('Os espaços com "v" podem ser preenchidos')
    NewGame = [['v', 'v', 'v'], ['v', 'v', 'v'], ['v', 'v', 'v']]
    return NewGame

def imprime(mat):
    print('\n')
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=' ')
        print('\n')

def entrada():
    print('\nDigite a linha ou coluna entre 1, 2 e 3')
    while True:
        linha = int(input('Posição da linha: '))
        if linha == 1 or linha == 2 or linha == 3:
            break
    while True:
        coluna = int(input('Posição da coluna: '))
        if coluna == 1 or coluna == 2 or coluna == 3:
            break
    return linha, coluna

def step(matriz, linha, coluna, simb):
    if matriz[linha-1][coluna-1] == 'v':
        matriz[linha - 1][coluna - 1] = simb
        return True
    else:
        print('\nPosição já ocupada, selecione outra posição\n')
        return False

def transposta(matriz):
    Transp = []
    for i in range(len(matriz[0])):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        Transp.append(linha)
    return Transp

def status(matriz):
    diagP = []
    diagS = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                diagP.append(matriz[i][j])
            if i+j == 2:
                diagS.append(matriz[i][j])
    if diagP == ['X', 'X', 'X']:
        return 2
    if diagP == ['O', 'O', 'O']:
        return 3
    if diagS == ['X', 'X', 'X']:
        return 2
    if diagS == ['O', 'O', 'O']:
        return 3
    for i in range(len(matriz)):
        if matriz[i] == ['X', 'X', 'X']:
            return 2
        if matriz[i] == ['O', 'O', 'O']:
            return 3
    mt = transposta(matriz)
    for i in range(len(mt)):
        if mt[i] == ['X', 'X', 'X']:
            return 2
        if mt[i] == ['O', 'O', 'O']:
            return 3

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'v':
                return 1
    return 0

def SalvarAnterior():
    try:
        Read = open('resultado_jogo_da_velha.txt', 'r')
        Arquivo = []
        for line in Read:
            save = line.rstrip()
            Arquivo.append(save)
        return Arquivo
    except FileNotFoundError:
        print('Arquivo não encontrado, será criado um novo arquivo')

def game():
    arqv = SalvarAnterior()
    t = True
    y = 0
    if arqv != None:
        while t == True:
            try:
                y += 1
                arqv[1+(9*y)] = str(int(arqv[1+(9*(y-1))]) + 1)
            except IndexError:
                t = False
    Record = open('resultado_jogo_da_velha.txt', 'w')
    if arqv != None:
                for x in range(len(arqv)):
                    Record.write(str(arqv[x]) + '\n')
    while True:
        print('\nDigite 0 para encerrar o programa ')
        print('Para um novo jogo, digite um número diferente de zero\n')
        parada = input('Entrada: ')
        if parada == '0':
            break
        else:
            jogo = initialize()
            imprime(jogo)
            print('\nEntre com X ou O')
            while True:
                player = input('Digite o simbolo do jogador: ').upper()
                if player =='X' or player == 'O':
                    break
            while True:
                lastplayer = player
                while True:
                    linha, coluna = entrada()
                    test = step(jogo, linha, coluna, player)
                    if test == True:
                        break
                imprime(jogo)
                resultado = status(jogo)
                if resultado == 0:
                    print('\nEssa rodada terminou em empate')
                    break
                elif resultado == 2:
                    print('O jogador do simbolo X ganhou')
                    break
                elif resultado == 3:
                    print('\nO jogador do simbolo O ganhou')
                    break
                else:
                    if lastplayer == 'X':
                        player = 'O'
                        print('Turno do jogador ', player)
                    elif lastplayer == 'O':
                        player = 'X'
                        print('Turno do jogador ', player)
                    print('\n')
            y += 1
            Record.write('Partida:' + '\n' + str(y) + '\n')
            
            for i in range(len(jogo)):
                for j in range(len(jogo[0])):
                    Record.write(str(jogo[i][j]) + '  ')
                Record.write('\n')
            if resultado == 0:
                Record.write('\nA partida terminou em empate\n')
            elif resultado == 2:
                Record.write('\nO jogador do simbolo X ganhou\n')
            elif resultado == 3:
                Record.write('\nO jogador do simbolo O ganhou\n')
            Record.write('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
game()