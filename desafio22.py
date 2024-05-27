nome = input('Digite seu nome: ').strip()

print('Nome tudo maiusculo: {}'.format(nome.upper()))
print('Nome tudo minusculo: {}'.format(nome.lower()))
print('Quantidade letras: {}'.format(len(nome.replace(' ','').strip())))
print('O 1 nome {} tem {} letras'.format(nome.split()[0],nome.find(' ')))