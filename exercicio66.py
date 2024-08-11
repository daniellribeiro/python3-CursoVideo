contador = 0
soma = 0
numero = 0
while True:
    numero = int(input('Digite um numero 999 - sair: '))

    if numero == 999:
        break

    soma += numero
    contador += 1

print(f'Foram digitados {contador} numeros, a soma e {soma}')