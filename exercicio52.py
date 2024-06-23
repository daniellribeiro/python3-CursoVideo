import math

numero = int(input('Digite um numero: '))

isPrimo = True
contador = 0

if numero <= 1:
    isPrimo = False
else:
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
            print(f'\033[33m {i} \033[m', end=' ')
        else:
            print(f'\033[31m {i} \033[m', end=' ')
if contador != 2:
    isPrimo = False

print('\n')
print('{}: {} primo'.format(numero, 'E' if isPrimo else 'Nao e'))

if numero > 1:
    print('Ele e divisivel {} vezes'.format(contador))
