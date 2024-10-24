from utilidadesCeV.moeda import moeda

numero = float(input('Digite um numero: '))
print(f'A metade e {moeda.moeda(moeda.metade(numero))}')
print(f'O dobro e {moeda.moeda(moeda.dobro(numero))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(numero, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(numero, 13))}')
