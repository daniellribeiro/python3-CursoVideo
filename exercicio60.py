numero = int(input('Digite um numero: '))
resultado = 1

print('{}! = '.format(numero),end='')
while numero > 1:
    resultado = resultado * numero
    print('{} x '.format(numero), end='')
    numero = numero - 1
print('1 = {}'.format(resultado))
