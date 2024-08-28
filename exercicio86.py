matriz = []
linha = []
numero = 0

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f'Digite o valor da posicao [{i}][{j}]: '))
        linha.append(numero)
    matriz.append(linha)
for i in matriz:
    for j in i:
        print(f'[{j}]',end='')
    print('')