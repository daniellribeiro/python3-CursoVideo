dicionario = {}
lista = []
for i in range(3):
    dicionario['numero'] = int(input('numero: '))
    lista.append(dicionario.copy())
print(lista)