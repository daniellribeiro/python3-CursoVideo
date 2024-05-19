#Desafio 11 - Ler largura e altura de uma parede em metros e calcular a area e a quantidade de tinta para pinta-la
#1 litro de tinta = 2 metros quadrados area pintada

import math

alturaParede = float(input('Digite a altura da parede em metros: '))

larguraParede = float(input('Digite a largura da parede em metros: '))

areaParede = alturaParede * larguraParede

print('A area da parede e : {} m²'.format(areaParede))

print('Serao usados aproximadamente {} litros de tinta'.format(math.ceil(areaParede / 2)))