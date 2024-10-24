def leiaInt():
    while True:
        try:
            n = input('Digite um numero inteiro: ')
            return int(n)
        except:
            print('Por favor digite um numero valido')


def leiaFloat():
    while True:
        try:
            n = input('Digite um numero real: ')
            return float(n)
        except:
            print('Por favor digite um numero real valido')

nInt = leiaInt()
nFloat = leiaFloat()

print(f'Vc digitou os numeros {nInt} e {nFloat}')