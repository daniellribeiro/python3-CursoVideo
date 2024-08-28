lista = []
numero = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('Valor duplicado nao vou adicionar!!!')
    else:
        lista.append(numero)
    if input('Deseja Sair S-SIM N-NAO: ') in 'Ss':
        break

print(f'Foram digitados {len(lista)} numeros')
print(sorted(lista))