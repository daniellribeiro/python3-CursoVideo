numerosLista = []
for i in range(4):
    numero = int(input(f'Digite o {i + 1} valor: '))
    numerosLista.append(numero)
numerosTupla = tuple(numerosLista)
print(numerosTupla)
print(f'O valor 9 apareceu  {numerosTupla.count(9)} vezes')
if 3 in numerosTupla:
    print(f'O valor 3 foi digitado na posicao {numerosTupla.index(3) + 1}')
else:
    print('O valor 3 nao foi digitado')

print('Os numeros pares sao: ',end=' ')
for i in numerosTupla:
    if i % 2 == 0:
        print(f'{i},',end=' ')