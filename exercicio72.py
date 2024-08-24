numerosExtenso = ('vazio','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
                  'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove')
numerosExtensoDezena = ('vazio','vazio','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa')
numerosExtensoCentena = ('vazio','cento','duzentos','trezentos','quantrocentos','quinhentos','seiscentos','setecentos',
                         'oitocentos','novecentos')

numero = int(input('Digite um numero: '))
numeroDezena = 0
numeroCentena = 0

if numero == 0:
    print('zero')
#Centena
if numero == 100:
    print('cem')
elif numero > 99 and numero < 1000:
    numeroCentena = numero // 100
    print(numerosExtensoCentena[numeroCentena],end=' ')
#Dezena
if numeroCentena > 0:
    numero-=(numeroCentena * 100)
    if numero != 0:
        print('e',end=' ')

if numero > 19 and numero < 100:
    numeroDezena = numero // 10
    print(numerosExtensoDezena[numeroDezena],end=' ')

#Unidade
if(numeroDezena > 0):
    numero -= (numeroDezena * 10)
    if numero != 0:
        print('e',end=' ')

if numero < 20 and numero > 0:
    print(numerosExtenso[numero])
