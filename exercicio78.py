lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    if input('Deseja Sair S-SIM N-NAO: ') in 'Ss':
        break

print(f'Foram digitados {len(lista)} numeros')
print(f'O maior valor e {max(lista)} nas posicoes ',end='')
for i ,v in enumerate(lista):
    if v == max(lista):
        print(f'...{i + 1}',end='')
print(f'\n O menor valor e {min(lista)} nas posicoes ',end='')
for i ,v in enumerate(lista):
    if v == min(lista):
        print(f'...{i + 1}',end='')