'''*
Entrega da prova N1 ___- Algoritmos e Programação II
Nós,

Leonardo Pinheiro de Souza
Thiago Aidar Figueiredo



*/'''

import random

def inicializarGrid():
    grid = [[' ','1','2','3','4','5','6','7','8','9','10'], ['A','.','.','.','.','.','.','.','.','.','.'],['B','.','.','.','.','.','.','.','.','.','.'],['C','.','.','.','.','.','.','.','.','.','.'],['D','.','.','.','.','.','.','.','.','.','.'],['E','.','.','.','.','.','.','.','.','.','.'],['F','.','.','.','.','.','.','.','.','.','.'],['G','.','.','.','.','.','.','.','.','.','.'],['H','.','.','.','.','.','.','.','.','.','.'],['I','.','.','.','.','.','.','.','.','.','.'],['J','.','.','.','.','.','.','.','.','.','.']]
    return grid

def imprimir(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='    ')
        print('\n')

def vert():
    while True:
        vertical = random.randint(0, 1)
        if vertical == 1:
            vertical = True
            break
        elif vertical == 0:
            vertical = False
            break
    return vertical

def posicionar_porta_avioes(grid,linha, coluna, vertical):
    teste = False
    if vertical == True:
        for i in range(linha, linha+5):
            if grid[i][coluna] != '.':
                return grid, teste
            else:
                grid[i][coluna] = 'P'

    elif vertical == False:
        for i in range(coluna, coluna+5):
            if grid[linha][i] != '.':
                return grid, teste
            else:
                grid[linha][i] = 'P'
    teste = True
    return grid, teste

def posicionar_encouracado(grid,linha, coluna, vertical):
    teste = False
    if vertical == True:
        for i in range(linha, linha+4):
            if grid[i][coluna] != '.':
                return grid, teste
            else:
                grid[i][coluna] = 'E'

    elif vertical == False:
        for i in range(coluna, coluna+4):
            if grid[linha][i] != '.':
                return grid, teste
            else:
                grid[linha][i] = 'E'
    teste = True
    return grid, teste

def posicionar_cruzador(grid,linha, coluna, vertical):
    teste = False
    if vertical == True:
        for i in range(linha, linha+3):
            if grid[i][coluna] != '.':
                return grid, teste
            else:
                grid[i][coluna] = 'C'

    elif vertical == False:
        for i in range(coluna, coluna+3):
            if grid[linha][i] != '.':
                return grid, teste
            else:
                grid[linha][i] = 'C'
    teste = True
    return grid, teste

def posicionar_submarino(grid,linha, coluna, vertical):
    teste = False
    if vertical == True:
        for i in range(linha, linha+2):
            if grid[i][coluna] != '.':
                return grid, teste
            else:
                grid[i][coluna] = 'S'

    elif vertical == False:
        for i in range(coluna, coluna+2):
            if grid[linha][i] != '.':
                return grid, teste
            else:
                grid[linha][i] = 'S'
    teste = True
    return grid, teste

def geraTabuleiro(grid):
    while True:
        vertical = vert()
        if vertical == True:
            linha = random.randint(1, 6)
            coluna = random.randint(1, 10)
        else:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 6)
        grid, teste = posicionar_porta_avioes(grid, linha, coluna, vertical)
        if teste == True:
            break

    while True:
        vertical = vert()
        if vertical == True:
            linha = random.randint(1, 7)
            coluna = random.randint(1, 10)
        else:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 7)
        grid, teste = posicionar_encouracado(grid, linha, coluna, vertical)
        if teste == True:
            break
        elif teste == False:
            for i in range(1, len(grid)):
                for j in range(1, len(grid[0])):
                    if grid[i][j] == 'E':
                        grid[i][j] = '.'
    while True:
        vertical = vert()
        if vertical == True:
            linha = random.randint(1, 8)
            coluna = random.randint(1, 10)
        else:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 8)
        grid, teste = posicionar_cruzador(grid, linha, coluna, vertical)
        if teste == True:
            break
        elif teste == False:
            for i in range(1, len(grid)):
                for j in range(1, len(grid[0])):
                    if grid[i][j] == 'C':
                        grid[i][j] = '.'
    while True:
        vertical = vert()
        if vertical == True:
            linha = random.randint(1, 9)
            coluna = random.randint(1, 10)
        else:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 9)
        grid, teste = posicionar_submarino(grid, linha, coluna, vertical)
        if teste == True:
            break
        elif teste == False:
            for i in range(1, len(grid)):
                for j in range(1, len(grid[0])):
                    if grid[i][j] == 'S':
                        grid[i][j] = '.'
    return grid


def atirar(grid, linha, coluna):
    if grid[linha][coluna] == '.':
        grid[linha][coluna] = 'x'
        print('Alvo atingido: água\n')
        return 'x'
    elif grid[linha][coluna] != '.' and grid[linha][coluna] != 'x' and grid[linha][coluna] != 'X':
        grid[linha][coluna] = 'X'
        print('Alvo atingido: embarcação\n')
        return 'X'

def main():
    while True:
        print('\nBem vindo ao jogo batalha naval\n')
        print('Digite 1 para começar um novo jogo')
        print('Digite 0 para encerrar o programa\n')
        menu = int(input('Entrada: '))
        if menu == 1:
            grid = inicializarGrid()
            imprimir(grid)
            grid = geraTabuleiro(grid)
            grid2 = inicializarGrid()
            cont = 0
            venceu = 0
            while cont < 20:
                while True:
                    while True:
                        linha = input('\nDigite a linha que deseja atacar (A - J): ').upper()
                        for x in range(1, len(grid[0])):
                            if grid[x][0] == linha:
                                linha = x
                        if linha > 0 and linha <= 10:
                            break
                        elif linha > 10:
                            print('Entrada Invalida\n')
                    while True:
                        coluna = int(input('Digite a coluna que deseja atacar (1 - 10): '))
                        if coluna > 0 and coluna <= 10:
                            break
                        elif linha > 10:
                            print('Entrada invalida\n')
                    x = atirar(grid, linha, coluna)
                    if x =='x' or x =='X':
                        cont += 1
                        break
                    else:
                        print('Posição já atacada\n')
                if x =='X':
                    venceu += 1
                    if venceu == 14:
                        print('\nParabéns, todas as embarcações foram destruídas, o jogo foi concluído!\n')
                        imprimir(grid)
                        break
                grid2[linha][coluna] = x
                imprimir(grid2)
                if cont == 20:
                    print('\nO jogo não foi concluído em 20 rodadas, tente novamente\n')
                    imprimir(grid)
                    print('Faltaram', 14 - venceu, 'a serem destruídas\n')
        elif menu == 0:
            break
        else:
            print('\nEntrada inválida\n')
main()
