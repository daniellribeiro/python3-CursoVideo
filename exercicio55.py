#Leia o peso de 5 pessoas, e informe o maior e menor peso

maiorPeso = 0
menorPeso = 10000

for i in range(0,5):
    peso = float(input('Digite seu peso: '))
    if(peso > maiorPeso):
        maiorPeso = peso
    if(peso < menorPeso):
        menorPeso = peso

print('O maior peso e {}'.format(maiorPeso))
print('O menor peso e {}'.format(menorPeso))