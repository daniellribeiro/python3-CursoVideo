#Ler 2 notas e falar se aluno foi aprovado

import metodoCores

funcoes = {
    'inicia': '\033[',
    'limpa': '\033[0m',
    'finaliza': 'm'
}

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

corVerde = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','verde','preto') +
       funcoes['finaliza'])

corVermelha = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','vermelho','preto') +
       funcoes['finaliza'])

corAmarelo = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','amarelo','preto') +
       funcoes['finaliza'])

print('Sua media e {:.1f}'.format(media))

if media >= 7.0:
    print('{}APROVADO!!!{}'.format(corVerde,funcoes['limpa']))
elif media < 5.0:
    print('{}REPROVADO!!!{}'.format(corVermelha,funcoes['limpa']))
else:
    print('{}RECUPERACAO!!!{}'.format(corAmarelo,funcoes['limpa']))