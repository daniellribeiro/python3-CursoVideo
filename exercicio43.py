#Calcular IMC

peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

IMC = peso / altura ** 2

resultado = ''

print('O seu IMC e {:.1f}'.format(IMC))

if IMC < 18.5:
    resultado = 'Abaixo do peso'
elif IMC > 40:
    resultado = 'Obesidade morbida'
elif IMC >= 18.5 and IMC < 25:
    resultado = 'Peso ideal'
elif IMC >= 25 and IMC < 30:
    resultado = 'Sobrepeso'
else:
    resultado = 'Obesidade'

print('Seu resultado e {}'.format(resultado))