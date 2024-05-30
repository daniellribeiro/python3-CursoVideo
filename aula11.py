print('\033[0;37;41mteste\033[0m')
print('\033[4;33;44mteste\033[0m')
print('\033[1;35;43mteste\033[0m')
print('\033[37;42mteste\033[0m')
print('\033[mteste\033[0m')
print('\033[7mteste\033[0m')

print('\033[4;45mOla, Mundo!\033[m')

print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(3,5))

nome = 'Daniel'
cores = {'limpa': '\033[m',
         'inicia': '\033[',
         'azul_sublinhado': '34:4m'}

cor = cores['inicia'] + cores['azul_sublinhado']

print('Ola {}{}{}'.format(cor,nome,cores['limpa']))
print('Ola {}'.format(cor + nome + cores['limpa']))

