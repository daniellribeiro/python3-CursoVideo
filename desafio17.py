#Ler o comprimento cateto oposto e o cateto adjacente de um triangulo e informar o comprimento da hipotenusa

import math

catetoOposto = float(input('Informe o comprimento do Cateto Oposto: '))

catetoAdjacente = float(input('Informe o comprimento do Cateto Adjacente: ' ))

#hipotenusa = math.sqrt(math.pow(catetoOposto,2) + math.pow(catetoAdjacente,2))

hipotenusa = math.hypot(catetoOposto,catetoAdjacente)

print('O comprimento da hipotenusa e {:.2f}'.format(hipotenusa))