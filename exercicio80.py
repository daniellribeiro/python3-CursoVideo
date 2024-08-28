lista = []
listaOriginal = []
numero = 0
for i in range(5):
    numero = int(input(f'Digite o {i+1}° numero: '))
    listaOriginal.append(numero)
    for i in range(len(listaOriginal)):
        lista.append(min(listaOriginal))
        listaOriginal.remove(min(listaOriginal))
    listaOriginal = lista
    lista = []
    print(f'Valor adicionado na posicao {listaOriginal.index(numero)} da lista')
print(listaOriginal)