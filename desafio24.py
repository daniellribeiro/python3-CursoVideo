cidade = input('Digite o nome de uma cidade: ').strip()

resposta = ''

if 'Santo'.upper() not in cidade.upper().split()[0]:
    resposta = ' nao'

print('A cidade {}{} comeca com o nome Santo'.format(cidade,resposta))