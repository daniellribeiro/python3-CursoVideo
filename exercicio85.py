numero = 0
lista = []
contadorOriginal = 0

for i in range(8):
    numero = int(input(f'Digite o {i + 1}º numero: '))
    lista.append(numero)

lista.sort()

print(f'Numeros Pares {[x for x in lista if x % 2 == 0]}')
print(f'Numeros Impares {[x for x in lista if x % 2 != 0]}')