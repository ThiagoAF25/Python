'''*
Entrega do Projeto 4 - Visualizacao Algoritmos de Ordenacao - Algoritmos e Programação II
Nós,

Leonardo Pinheiro de Souza
TIA:32127391

Thiago Aidar Figueiredo
TIA:32144547

*/'''

import random
import pygame

def geraLista(n):
    lista = [0] * n
    for i in range(n):
        lista[i] = random.randint(1,9)
    return lista

def partition(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            pygame.event.wait()
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def QuickSort(lista, inicio, fim, screen):
    colorRect= (0,122,255)
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        screen.fill((255,255,255))
        x = 10
        for i in range(len(lista)):
            if i == inicio:
                pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))     
            elif i == pivo:
                pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))
            else:
                pygame.draw.rect(screen, colorRect, (x,450 - (30 * lista[i]),25,30 * lista[i])) 
            x += 35
        pygame.display.update()
        pygame.time.wait(350)
        QuickSort(lista, inicio, pivo - 1, screen)
        screen.fill((255,255,255))
        x = 10
        for i in range(len(lista)):
            if i == pivo:
                pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))     
            elif i == fim:
                pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))  
            else:
                pygame.draw.rect(screen, colorRect, (x,450 - (30 * lista[i]),25,30 * lista[i])) 
            x += 35
        pygame.display.update()
        pygame.time.wait(350)
        QuickSort(lista, pivo + 1, fim, screen)
        
def Inicio(lista, screen, color):
    x = 10
    for i in range(len(lista)):
        pygame.draw.rect(screen, color, (x,450 - (30 * lista[i]),25,30 * lista[i])) 
        x += 35

def Troca(lista, screen, color, salvo):
    x = 10
    for i in range(len(lista)):
        if i == salvo:
            pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))
        else:    
            pygame.draw.rect(screen, color, (x,450 - (30 * lista[i]),25,30 * lista[i])) 
        x += 35

def QUICK():
    lista = geraLista(15)
    pygame.init()
    screen = pygame.display.set_mode((600,450))
    pygame.display.set_caption("Quick Sort")

    screen.fill((255,255,255))
    colorRect = (0,122,255) 
    Inicio(lista,screen,colorRect)

    pygame.display.update()
    pygame.time.wait(350)

    QuickSort(lista, 0, len(lista) - 1, screen)

def BUBBLE():
    pygame.init()
    screen = pygame.display.set_mode((600,450))
    vet = geraLista(15)
    
    pygame.display.set_caption("Bubble Sort")
    screen.fill((255,255,255))
    colorRect = (0,122,255)
    Inicio(vet,screen,colorRect)
    
    for k in range(len(vet)):
        for i in range(len(vet)-1-k):
            salva = len(vet)
            if vet[i] > vet[i+1]:
                aux = vet[i]
                vet[i] = vet[i+1]
                vet[i+1] = aux
                salva = i + 1
                pygame.mixer.music.load('ponto.wav')
                pygame.mixer.music.play()
                pygame.event.wait()
            screen.fill((255,255,255))
            Troca(vet,screen, colorRect, salva)
            pygame.time.delay(150)
            pygame.display.update()

def SELECT():
    pygame.init()
    screen = pygame.display.set_mode((600,450))
    vet = geraLista(15)

    pygame.display.set_caption("Selection Sort")
    screen.fill((255,255,255))
    colorRect = (0,122,255)
    Inicio(vet,screen,colorRect)
    
    for i in range(len(vet)):
        min = i
        salva = len(vet)+1
        for j in range(i+1, len(vet)):
            if vet[min] > vet[j]:
                min = j
                salva = min
                pygame.mixer.music.load('ponto.wav')
                pygame.mixer.music.play()
                pygame.event.wait()
        aux = vet[i]
        vet[i] = vet[min]
        vet[min] = aux
        screen.fill((255,255,255))
        Troca(vet,screen, colorRect, salva)
        pygame.time.delay(400)
        pygame.display.update()

def INSERT():
    pygame.init()
    screen = pygame.display.set_mode((600,450))
    vet = geraLista(15)

    pygame.display.set_caption("Insertion Sort")
    screen.fill((255,255,255))
    colorRect = (0,122,255)
    Inicio(vet,screen,colorRect)

    for i in range(1, len(vet)):
        x = vet[i]
        j = i - 1
        salva = len(vet)+1
        while j >= 0 and x < vet[j]:
            vet[j+1] = vet[j]
            j -= 1
            salva = i
            pygame.mixer.music.load('ponto.wav')
            pygame.mixer.music.play()
            pygame.event.wait()
        vet[j+1] = x
        screen.fill((255,255,255))
        Troca(vet,screen, colorRect, salva)
        pygame.time.delay(400)
        pygame.display.update()

def Mergesort(lista, inicio, fim, screen):
    colorRect = ((0, 122, 255))
    if (fim - inicio) > 1:
        meio = (inicio + fim) // 2
        Mergesort(lista, inicio, meio, screen)
        screen.fill((255,255,255))
        x = 10
        for i in range(len(lista)):
            if i >= inicio and i< meio:
                pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))
            else:
                pygame.draw.rect(screen, colorRect, (x,450 - (30 * lista[i]),25,30 * lista[i]))
            x += 35
        pygame.display.update()
        pygame.time.wait(400)
        Mergesort(lista, meio, fim, screen)
        screen.fill((255,255,255))
        x = 10
        for i in range(len(lista)):
            if i >= meio and i< fim:
                pygame.draw.rect(screen, (255,0,0), (x,450 - (30 * lista[i]),25,30 * lista[i]))
            else:
                pygame.draw.rect(screen, colorRect, (x,450 - (30 * lista[i]),25,30 * lista[i]))
            x += 35
        pygame.display.update()
        pygame.time.wait(400)
        Merge(lista, inicio, meio, fim)
        screen.fill((255,255,255))
        x = 10
        for i in range(len(lista)):
            pygame.draw.rect(screen, colorRect, (x,450 - (30 * lista[i]),25,30 * lista[i]))
            x += 35
        pygame.display.update()
        pygame.time.wait(1500)

def Merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    top_e, top_d = 0, 0
    for k in range(inicio, fim):
        if top_e >= len(esquerda):
            lista[k] = direita[top_d]
            top_d += 1
        elif top_d >= len(direita):
            lista[k] = esquerda[top_e]
            top_e += 1
            save = k 
        elif esquerda[top_e] < direita[top_d]:
            lista[k] = esquerda[top_e]
            top_e += 1
            pygame.mixer.music.load('ponto.wav')
            pygame.mixer.music.play()
            pygame.event.wait()
        else:
            lista[k] = direita[top_d]
            top_d += 1
            pygame.mixer.music.load('ponto.wav')
            pygame.mixer.music.play()
            pygame.event.wait()

def MERGE():

    pygame.init()
    screen = pygame.display.set_mode((600,450))
    vet = geraLista(16)

    pygame.display.set_caption("Merge Sort")
    screen.fill((255,255,255))
    colorRect = (0,122,255)
    Inicio(vet,screen,colorRect)
    inicio = 0
    fim = len(vet)
    Mergesort(vet, inicio, fim, screen)

def main():
    BUBBLE()
    INSERT()
    SELECT()
    MERGE()
    QUICK()
    pygame.quit()

main()