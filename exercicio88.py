from random import randint

quantJogos = int(input('Quantos Jogos vc ira jogar ?: '))
matriz = []
linha = []
for i in range(quantJogos):
    linha = []
    for j in range(6):
        linha.append(randint(0,60))
    matriz.append(linha)
for linha in matriz:
    for i in linha:
        print(f'[{str(i):^5}]',end='')
    print('',end='\n')