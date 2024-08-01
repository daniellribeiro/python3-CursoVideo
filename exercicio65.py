continuar = 'S'
numero = maiorNumero = menorNumero = media = contador = soma = 0

while continuar in ('Ss'):
    numero = int(input('Digite um outro numero: '))
    continuar = input('Deseja continuar S - Sim N - Nao : ')

    if(contador == 0):
        maiorNumero = menorNumero = numero
    elif(maiorNumero < numero):
        maiorNumero = numero
    elif(menorNumero > numero):
        menorNumero = numero
    contador += 1
    soma+=numero

print('Contador: {}'.format(contador))
print('Maior Numero: {}'.format(maiorNumero))
print('Menor Numero: {}'.format(menorNumero))
print('A media e {}'.format(soma / contador))