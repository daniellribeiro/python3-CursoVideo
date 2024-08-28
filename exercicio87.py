matriz = []
linha = []
numero = 0
pares = 0
soma3Coluna = 0
maiorValor2Linha = 0
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f'Digite o valor da posicao [{i}][{j}]: '))
        linha.append(numero)
    matriz.append(linha)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]}]',end='')
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            soma3Coluna+=matriz[i][j]
        if (i == 1 and matriz[i][j] > maiorValor2Linha) or maiorValor2Linha == 0:
            maiorValor2Linha=matriz[i][j]
    print('')

print(f'A soma dos numeros pares é {pares}')
print(f'A soma dos numeros da 3 coluna é {soma3Coluna}')
print(f'Maior valor 2 linha é {maiorValor2Linha}')
