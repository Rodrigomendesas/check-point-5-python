
#------Integrantes-----
# Luana de Sousa - RM552621
# Matheus de Freitas - RM552602
# Rodrigo Mendes - RM553448

import random

def preencher_campo():
    #Gera uma matriz com 30 '*' (bombas) e 70 '-' (espaços vazios).
    campo = [['-' for i in range(10)] for i in range(10)]
    bombas = 30
    while bombas > 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if campo[x][y] != '*':
            campo[x][y] = '*'
            bombas -= 1
    return campo

def contar_vizinhos(campo, x, y):
    #Função que conta os vizinhos de cada indice da matriz (Campo)
    count = 0
    for i in range(max(0, x - 1), min(10, x + 2)):
        for j in range(max(0, y - 1), min(10, y + 2)):
            if campo[i][j] == '*' and (i, j) != (x, y):
                count += 1
    return count

def contar_bombas(campo):
    #Função que conta as bombas e gera uma nova matriz utilizando a função que conta os vizinhos
    segundo_campo = [[0 for i in range(10)] for i in range(10)]
    for i in range(10):
        for j in range(10):
            if campo[i][j] != '*':
                segundo_campo[i][j] = contar_vizinhos(campo, i, j)
    return segundo_campo

def exibir_campo(campo):
    #Formata a matrir ao imprimir
    print()
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            print(campo[i][j], end='\t')
        print()

campo = preencher_campo()

print("\nCampo com bombas: ")
exibir_campo(campo)

campo_numero = contar_bombas(campo)

print("\nCampo numerado: ")
exibir_campo(campo_numero)
