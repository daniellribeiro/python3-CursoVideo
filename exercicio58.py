import random
from time import sleep

i = 10
palpites = 0

def imprimirRiscos():
      print('-=-' * 20)

imprimirRiscos()
print('Vou pensar em um numero de 0 a {}, tente adivinhar!'.format(i))
imprimirRiscos()

numeroSorteado = random.randint(0,i)
numeroEscolhido = i + 1

while numeroSorteado != numeroEscolhido:
    palpites+=1

    numeroEscolhido = int(input('Digite um numero inteiro entre 0 e {}: '.format(i)))

    print('PROCESSANDO....')
    sleep(3)

    if numeroSorteado==numeroEscolhido:
        print('Parabens vc acertou o numero sorteado')
    elif numeroSorteado > numeroEscolhido:
        print('Mais... Tente outra vez')
    else:
        print('Menos... Tente outra vez')

print('Voce levou {} palpites para adivinhar'.format(palpites))