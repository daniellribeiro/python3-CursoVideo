num1 = float(input('Digite o 1 numero: '))
num2 = float(input('Digite o 2 numero: '))
num3 = float(input('Digite o 3 numero: '))

if num1 < num2 and num1 < num3:
    menorNumero = num1
elif num2 < num1 and num2 < num3:
    menorNumero = num2
else:
    menorNumero = num3

if num1 > num2 and num1 > num3:
    maiorNumero = num1
elif num2 > num1 and num2 > num3:
    maiorNumero = num2
else:
    maiorNumero = num3

print('O menor numero e {}'.format(menorNumero))
print('O maior numero e {}'.format(maiorNumero))