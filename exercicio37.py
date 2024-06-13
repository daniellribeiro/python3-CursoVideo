#Ler um numero e convete-lo para binario, octal e hexadecimal

numero = int(input('Digite um numero: '))
print('Decimal: {}'.format(numero))
print('Binario: {}'.format(bin(numero)[3:] if (numero < 0) else bin(numero)[2:]))
print('Hexadecimal: {}'.format((hex(numero)[3:] if (numero < 0) else hex(numero)[2:])).upper())
print('Octal: {}'.format(oct(numero)[3:] if (numero < 0) else oct(numero)[2:]))
