lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    if input('Deseja Sair S-SIM N-NAO: ') in 'Ss':
        break

print(f'Foram digitados {len(lista)} numeros')
print(f'O numero cinco{'' if lista.count(5) > 0 else ' nao'} foi digitado')
print(f'Ordem descrescente: {sorted(lista,reverse=True)}')