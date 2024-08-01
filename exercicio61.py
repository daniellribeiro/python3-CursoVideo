numero1 = int(input('Digite 1 termo: '))

razao = int(input('Digite a razao da PA: '))

resultado = 0
i=0

while i < 10:
    resultado = numero1 + i * razao
    print(resultado,end=' ')
    i = i + 1
