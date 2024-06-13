#Ler 2 numeros e falar qual e o maior

numero1 = int(input('Digite um numero: '))

numero2 = int(input('Digite outro numero: '))

if(numero1 > numero2):
    print('O 1 valor e maior')
elif(numero1 < numero2):
    print('O 2 valor e maior')
else:
    print('Os valores sao iguais')