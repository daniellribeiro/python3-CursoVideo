import random
from time import sleep

def imprimirRiscos():
      print('-=-' * 20)

imprimirRiscos()
print('Vou pensar em um numero de 0 a 5, tente adivinhar!')
imprimirRiscos()

numeroSorteado = random.randint(0,5)

numeroEscolhido = int(input('Digite um numero inteiro entre 0 e 5: '))

print('PROCESSANDO....')
sleep(3)

print('Parabens vc acertou o numero sorteado' if numeroSorteado == numeroEscolhido
      else 'Infelizmente o numero sorteado foi {}'.format(numeroSorteado))