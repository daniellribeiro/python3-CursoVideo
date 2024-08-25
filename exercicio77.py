palavras = ('bicicleta','armario','cama','carro','urso')

for i in palavras:
    print(f'{i} ==>> ',end=' ')
    if 'A' in i.upper():
        print('A',end=' ')
    if 'E' in i.upper():
        print('E',end=' ')
    if 'I' in i.upper():
        print('I',end=' ')
    if 'O' in i.upper():
        print('O',end=' ')
    if 'U' in i.upper():
        print('U',end=' ')
    print('\n')