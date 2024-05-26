#Ler o valor de um angulo e calcular seu seno, cosseno e tangente

import math

num = float(input('Digite um angulo: '))

print('Seno: {:.2f}'.format(math.sin(math.radians(num))))
print('Cosseno: {:.2f}'.format(math.cos(math.radians(num))))
print('Tangente: {:.2f}'.format(math.tan(math.radians(num))))
