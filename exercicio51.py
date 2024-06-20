numero1 = int(input('Digite 1 termo: '))

razao = int(input('Digite a razao da PA: '))

resultado = 0
for i in range(1,11):
    resultado = numero1 + (i - 1) * razao
    print(resultado)
