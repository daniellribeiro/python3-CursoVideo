#Ler a idade de 7 pessoas e falar que é maior de idade, e quem ainda nao e

maiorIdade = 0
menorIdade = 0

for i in range(0,7):
    idade = int(input('Digite sua idade: '))
    if idade > 17:
        maiorIdade += 1
    else:
        menorIdade += 1

print('{} pessoas sao maior de idade'.format(maiorIdade))
print('{} pessoas sao menor de idade'.format(menorIdade))