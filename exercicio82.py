lista = []
numerosPares = []
numerosImpares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    if input('Deseja Sair S-SIM N-NAO: ') in 'Ss':
        break

for numero in lista:
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)

print(f'Numeros {sorted(lista)}')
print(f'Numeros Pares {sorted(numerosPares)}')
print(f'Numeros Impares {sorted(numerosImpares)}')