numero = int(input('Digite um numero: '))
resultado = 1

print('{}! = '.format(numero),end='')

for i in range(numero,1,-1):
    resultado = resultado * i
    print('{} x '.format(i), end='')
print('1 = {}'.format(resultado))
