valorOriginal = 0
valor = 0
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas1 = 0
while True:
    valor = int(input('Qual valor deseja sacar: '))
    valorOriginal = valor
    cedulas50 = 0
    cedulas20 = 0
    cedulas10 = 0
    cedulas1 = 0
    while valor > 0:
        if valor >= 50:
           cedulas50 += 1
           valor -= 50
        elif valor >= 20:
           cedulas20 += 1
           valor -= 20
        elif valor >= 10:
            cedulas10 += 1
            valor -= 10
        elif valor >= 1:
            cedulas1 += 1
            valor -= 1

    print(f'O valor {valorOriginal}')
    if(cedulas50 > 0):
        print(f'{cedulas50} cedulas de 50')
    if(cedulas20 > 0):
        print(f'{cedulas20} cedulas de 20')
    if(cedulas10 > 0):
        print(f'{cedulas10} cedulas de 10')
    if(cedulas1 > 0):
        print(f'{cedulas1} cedulas de 1')

    if(input('Deseja realizar outro saque S-SIM N-NAO: ') in ('Nn')):
        break