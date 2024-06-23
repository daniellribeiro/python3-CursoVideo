#Ler a idade de 7 pessoas e falar que é maior de idade, e quem ainda nao e
import datetime

maiorIdade = 0
menorIdade = 0


anoAtual = datetime.date.today().year

for i in range(0,7):
    anoNascimento = int(input('Digite sua data nascimento: '))
    idade = anoAtual - anoNascimento

    if idade >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1

print('{} pessoas sao maior de idade'.format(maiorIdade))
print('{} pessoas sao menor de idade'.format(menorIdade))