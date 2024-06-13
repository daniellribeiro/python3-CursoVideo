#Criar jogo jokenpo
import random

import metodoCores

funcoes = {
    'inicia': '\033[',
    'limpa': '\033[0m',
    'finaliza': 'm'
}

corVenceu = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','verde','preto') +
       funcoes['finaliza'])

corPerdeu = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','vermelho','preto') +
       funcoes['finaliza'])

corEmpate = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','amarelo','preto') +
       funcoes['finaliza'])

itens = ('Pedra','Papel','Tesoura')

escolhaUsuario = int(input('Escolha 0 - Pedra / 1 - Papel / 2 - Tesoura : '))

escolhaComputador = random.randint(0,2)

if escolhaUsuario == escolhaComputador:
    print('Computador tambem escolheu {}, ocorreu {}Empate{}'.format(itens[escolhaComputador],corEmpate,funcoes['limpa']))
elif ((escolhaUsuario == 0 and escolhaComputador == 2) or
    (escolhaUsuario == 1 and escolhaComputador == 0) or
    (escolhaUsuario == 2 and escolhaComputador == 1)):
    print('Voce {}ganhou{} o computador escolheu {}'.format(corVenceu,funcoes['limpa'],itens[escolhaComputador]))
else:
    print('Voce {}perdeu{} o computador escolheu {}'.format(corPerdeu,funcoes['limpa'],itens[escolhaComputador]))