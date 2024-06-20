#Numero 1 a 500, que sao impares e multiplos de 3
#Depois some os numeros retornados
s = 0;
for i in range(1,501):
    if (i % 2 != 0) and (i % 3 == 0):
        print(i)
        s += i
print('A soma e {}'.format(s))
