def leiaInt(n = input('Digite um numero: ')):
    return n.isnumeric()


print(f'O valor digitado {'E' if leiaInt() else 'Nao e'} um numero')