valorOriginal = valor = cedula = contadorCedulas = 0
while True:
    valor = int(input('Qual valor deseja sacar: '))
    valorOriginal = valor
    print(f'O valor sacado e {valorOriginal}')
    cedula = 50
    while True:
        if valor >= cedula:
           contadorCedulas += 1
           valor -= cedula
        else:
            if contadorCedulas > 0:
                print(f'{contadorCedulas} de {cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            contadorCedulas = 0
            if valor == 0:
                break
    if(input('Deseja realizar outro saque S-SIM N-NAO: ') in ('Nn')):
        break