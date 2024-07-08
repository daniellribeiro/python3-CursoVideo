numero1 = int(input('Digite 1 termo: '))

razao = int(input('Digite a razao da PA: '))

resultado = 0
for i in range(0,10):
    resultado = numero1 + i * razao
    print(resultado,end=' ')
