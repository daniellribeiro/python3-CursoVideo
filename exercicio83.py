expressao = input('Digite uma expressao: ')

if expressao.count('(') == expressao.count(')'):
    print('Expresao valida')
else:
    print('Expressao invalida')