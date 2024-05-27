nome = input('Digite seu nome: ')
if nome=='Gustavo':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome nao e Gustavo!')
print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
media = (n1 + n2) / 2

print('A sua media e {}'.format(media))

if media >= 6.0:
    print('Sua media foi boa')
else:
    print('Vc precisa estudar mais')

print('PARABENS' if media >= 6.0 else 'ESTUDE MAIS')