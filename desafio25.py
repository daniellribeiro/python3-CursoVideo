nome = input('Digite o nome de uma pessoa: ').strip()

resposta = ''

if 'SILVA' not in nome.upper():
    resposta = ' nao'

print('{}{} tem Silva no nome'.format(nome,resposta))