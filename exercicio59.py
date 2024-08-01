numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

opcao = 0

while opcao != 5:
    print('Voce gostaria de: ')
    print('1 - Somar / 2 - Multiplicar / 3 - Maior / 4 - Novos numeros / 5 - Sair do programa ')
    opcao = int(input('Escolha uma opcao: '))

    if opcao==1:
        print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))
    elif opcao==2:
        print('{} * {} = {}'.format(numero1,numero2, numero1 * numero2))
    elif opcao==3:
        print('Dentre {} e {}, o maior numero e {}'.format(numero1,numero2,numero1 if numero1 > numero2 else numero2))
    elif opcao==4:
        numero1 = int(input('Digite um numero: '))
        numero2 = int(input('Digite outro numero: '))
    elif opcao==5:
        print('Saindo do programa....')
    else:
        print('Opcao invalida!!!')
