import math

numero = int(input('Digite um numero: '))

isPrimo = True

if numero <= 1:
    isPrimo = False
elif numero == 2 or numero == 3:
    isPrimo = True
elif numero % 2 == 0 or numero % 3 == 0:
    isPrimo = False
else:
    for i in range(4,numero):
        if(numero % i == 0):
            isPrimo = False
            break

print('{}: {} primo'.format(numero,'E' if isPrimo else 'Nao e'))


