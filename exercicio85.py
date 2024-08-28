numero = 0
lista = []
contadorOriginal = 0
contador = 0

for i in range(8):
    numero = int(input(f'Digite o {i + 1}º numero: '))
    lista.append(numero)
    if numero % 2 == 0:
        contadorOriginal+=1
    contador = 0
    for i in sorted(lista):
        lista.remove(i)
        if i % 2 == 0:
            lista.insert(contador,i)
            contador+=1
        else:
            lista.append(i)
    print(f'Numero foi inserido na posicao {lista.index(i)}')
print(lista)
print(f'Numeros Pares {[x for x in lista if x % 2 == 0]}')
print(f'Numeros Impares {[x for x in lista if x % 2 != 0]}')