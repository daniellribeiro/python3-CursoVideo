sexo = 'X'
while sexo not in 'MmFf':
    sexo = input('Digite seu sexo M ou F: ')
    if sexo in 'MFmf':
        print('Sexo {} registrado com sucesso'.format(sexo.upper()))
        sair = 1
    else:
        print('Opcao invalida!!!!')