numero3Posicao = 0
numerosLista = []
for i in range(5):
    numero = int(input(f'Digite o {i + 1} valor: '))
    numerosLista.append(numero)
    numerosTupla = tuple(numerosLista)
print(numerosTupla)
print(f'O valor 9 apareceu  {numerosTupla.count(9)} vezes')
if numero3Posicao > 0:
    print(f'O 1 valor 3 foi digitado na posicao {numero3Posicao}')
else
    print('O valor 3 nao foi digitado')

print('Os numeros pares sao: ',end=' ')
for i in numerosTupla:
    if i % 2 == 0:
        print(f'{i},',end=' ')