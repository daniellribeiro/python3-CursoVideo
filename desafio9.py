#desafio 9 - mostrar tabuada
numero = int(input('Digite o numero: '))

print('tabuada:')

for i in range(11):
    print('{} * {:>2} = {:0>2}'.format(numero,i,numero*i))