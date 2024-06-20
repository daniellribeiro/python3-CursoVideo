#Ler 6 numeros e somar os pares

s = 0
for i in range(0,6):
    n = int(input('Digite 1 numero: '))
    if n % 2 == 0:
        s += n
print('A soma dos pares e {}'.format(s))
