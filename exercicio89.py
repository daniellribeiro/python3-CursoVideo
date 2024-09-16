contador = 0
matriz = []
linha = []
contador = 0
indice = 0
media = 0

import math

while True:
    linha = []
    linha.append(input('Digite o nome do aluno: '))
    linha.append(float(input('Digite a 1 nota: ')))
    linha.append(float(input('Digite a 2 nota: ')))

    matriz.append(linha)

    if input('Deseja sair S- SIM: ') in 'Ss':
        break
print('N         Nome       Media')
for linha in matriz:
    media = round((linha[1] + linha [2])/ 2,1)
    print(f'{contador} {"{:^20}".format(linha[0])}{media}')
    contador+=1

while True:
    indice = int(input('Digite o numero do aluno que vc quer ver a nota: '))
    print(f'Nome: {matriz[indice][0]},', end=' ')
    print(f'nota 1 = {round(matriz[indice][1],1)},', end='')
    print(f'nota 2 = {round(matriz[indice][2],1)}', end='')
    media = round((matriz[indice][1] + matriz[indice][2]) / 2, 1)
    print(f' Media: {media}')
    if input('Deseja sair S- SIM: ') in 'Ss':
        break