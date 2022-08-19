import random

def main():
    while True:
        print('Entre com o tamanho da lista para continuar jogando ou -1 para encerrar o programa')
        n = int(input('Tamanho da lista: '))
        if n == -1:
            break
        else:
            num = [0] * n
            for i in range(len(num)):
                num[i] = random.randint(0, 9)
            Entrada(n, num)
            while True:
                print('\n1 - Jogador 1, 2 - Jogador 2')
                jogador = int(input('Quem começara jogando? '))
                if jogador == 1 or jogador == 2:
                    break
                else:
                    print('Entrada Invalida\n')
            vencedor = bolha(num, jogador)
            Saida(vencedor)

def Entrada(n, vet):
    try:
        SalvarE = open('Entrada.txt', 'r')
        texto = []
        for line in SalvarE:
            linha = line.rstrip()
            texto.append(linha)
        ImprimeE = open('Entrada.txt', 'w')
        for x in range(len(texto)):
            ImprimeE.write(texto[x] + '\n')
        write = (str(n))
        for i in range(len(vet)):
            write += ' ' + str(vet[i])
        ImprimeE.write(write)
    except FileNotFoundError:
        write = (str(n))
        ImprimeE = open('Entrada.txt', 'w')
        for i in range(len(vet)):
            write += ' ' + str(vet[i])
        ImprimeE.write(write)

def Saida(vencedor):
    try:
        SalvarS = open('saida.txt', 'r')
        texto = []
        for line in SalvarS:
            linha = line.rstrip()
            texto.append(linha)
        ImprimeS = open('saida.txt', 'w')
        for x in range(len(texto)):
            ImprimeS.write(texto[x] + '\n')
        ImprimeS.write(vencedor)
    except FileNotFoundError:
        ImprimeS = open('saida.txt', 'w')
        ImprimeS.write(vencedor)

def bolha(vet, jogador):
    troca = 0
    for k in range(len(vet)):
        for i in range(len(vet) - 1 - k):
            if vet[i] > vet[i + 1]:
                aux = vet[i]
                vet[i] = vet[i + 1]
                vet[i + 1] = aux
                troca += 1
    if jogador == 1:
        if troca % 2 == 1:
            return 'Jogador 1'
        else:
            return 'Jogador 2'
    if jogador == 2:
        if troca % 2 == 1:
            return 'Jodador 2'
        else:
            return 'Jogador 1'

main()