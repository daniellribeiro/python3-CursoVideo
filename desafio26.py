frase = input('Digite uma frase: ').strip().upper()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela 1 vez na posicao {}'.format(frase.find('A') + 1))
print('A letra A aparece pela ultima vez na posicao {}'.format(frase.rfind('A') + 1))
