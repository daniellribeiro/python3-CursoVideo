from utilidadesCeV.moeda import moeda

numero = int(input('Digite um numero: '))
print(f'A metade e {moeda.metade(numero, True)}')
print(f'O dobro e {moeda.dobro(numero, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(numero, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(numero, 13, True)}')
