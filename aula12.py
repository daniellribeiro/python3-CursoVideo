nome = input('Qual e o seu nome ? ')

if nome == 'Daniel':
    print('Que nome bonito!!!')
elif nome in 'Pedro Maria Paulo':
    print('Seu nome e bem popular no Brasil')
else:
    print('Seu nome e bem normal!!!')

print('Tenha um bom dia {}'.format(nome))