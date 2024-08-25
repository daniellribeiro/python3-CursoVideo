from random import randint
numerosLista = []
for i in range(5):
    numerosLista.append(randint(0,100))
numerosTupla = tuple(numerosLista)
print(numerosTupla)
print(f'O maior valor e {max(numerosTupla)}')
print(f'O menor valor e {min(numerosTupla)}')