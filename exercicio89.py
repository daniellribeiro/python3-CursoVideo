contador = 0
matriz = []
linha = []
contador = 0
indice = 0
while True:
    linha = []
    linha.append(input('Digite o nome do aluno: '))
    linha.append(float(input('Digite a 1 nota: ')))
    linha.append(float(input('Digite a 2 nota: ')))

    matriz.append(linha)

    if input('Deseja sair S- SIM: ') in 'Ss':
        break
print('N         Nome     Media')
for linha in matriz:
    print(f'{contador} {"{:^20}".format(linha[0])}{(linha[1] + linha[2]) / 2}')
    contador+=1

while True:
    indice = int(input('Digite o numero do aluno que vc quer ver a nota: '))
    print(f'Nome: {matriz[indice][0]}, nota 1 = {matriz[indice][1]}, nota 2 = {matriz[indice][2]}',end='')
    print(f' Media: {(matriz[indice][1] + matriz[indice][2]) / 2}')
    if input('Deseja sair S- SIM: ') in 'Ss':
        break