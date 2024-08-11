numero = 0
while True:
    numero = int(input('Digite um numero: '))

    if numero < 0:
        break

    for i in range(11):
        print(f'{numero} X {i} = {numero * i}')