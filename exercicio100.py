from random import randint

numeros = []

def sorteio():
    return randint(0,100)

def pares(lista):
    aux = []
    for i in lista:
        if i % 2 == 0:
            aux.append(i)
    print(f'A soma dos pares e {sum(aux)}')
    return aux

for i in range(5):
    numeros.append(sorteio())

print(f'Os numeros sorteados sao {numeros}')
print(f'Os numeros pares sao {pares(numeros)}')