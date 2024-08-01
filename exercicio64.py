soma = contador = 0

numero = int(input('Digite um numero: '))

while numero != 999:
    contador+=1
    soma+=numero
    numero = int(input('Digite um numero: '))
print('O somatorio e {}'.format(soma))
print('Foram digitados {} numeros'.format(contador))
