import math

velocidade = float(input('Qual a sua velocidade: '))

if(velocidade <= 80.0):
    print('Parabens vc esta dentro do limite de velocidade de 80 km/h')
else:
    ultrapassou = math.floor(velocidade - 80.0)
    print('Vc ultrapassou {} km/h do limite, vc sera multado em R${} reais'.format(ultrapassou,ultrapassou * 7.0))