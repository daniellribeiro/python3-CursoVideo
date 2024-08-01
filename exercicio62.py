numero1 = int(input('Digite 1 termo: '))

razao = int(input('Digite a razao da PA: '))

resultado = 0
i=0
maximo = 10

while i < maximo:
    resultado = numero1 + i * razao
    print(resultado,end=' ')
    i = i + 1
    if i==maximo:
        print('\n')
        maisTermos = int(input('Mostro mais quantos termos ?: '))
        maximo+=maisTermos

        if maisTermos > 0:
            i = 0
print('A progressao foi finalizada com {} termos mostrados'.format(i))
