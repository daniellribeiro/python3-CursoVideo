matriz = []
linha = []
numero = maiorNumero = contador = numeroDigitos = 0

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f'Digite o valor da posicao [{i}][{j}]: '))
        linha.append(numero)
        if maiorNumero < numero or contador == 0:
            maiorNumero = numero
        contador+=1
    matriz.append(linha)

numeroDigitos = len(str(maiorNumero))
for i in matriz:
    texto_formatado = ''
    for j in i:
        texto_formatado = f"{str(j):^{numeroDigitos}}"
        print(f'[{texto_formatado}]',end='')
    print('')