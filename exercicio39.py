#Ler idade de um jovem e informar se ele deve se alistar no Tiro Guerra

import metodoCores
from datetime import datetime

funcoes = {
    'inicia': '\033[',
    'limpa': '\033[0m',
    'finaliza': 'm'
}

corVerde = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','verde','preto') +
       funcoes['finaliza'])

corVermelha = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','vermelho','preto') +
       funcoes['finaliza'])

anoNascimento = int(input('Qual o ano que voce nasceu: '))

anoAtual = datetime.now().year

idade = anoAtual - anoNascimento

print('Voce tem {} anos'.format(idade))

if(idade < 18):
    print('Voce se alistara no servico militar daqui a {}{}{} anos'.format(corVerde,18 - idade, funcoes['limpa']))
    print('Seu alistamento sera no ano de {}'.format(anoAtual + (18 - idade)))
elif(idade > 18):
    print('Ja passou {}{}{} anos do tempo do seu alistamento'.format(corVermelha, idade - 18, funcoes['limpa']))
    print('Seu alistamento deveria ter sido no ano de {}'.format(anoAtual - (idade - 18)))
else:
    print('{} Chegou a idade de se alistar!!! {}'.format(corVerde,funcoes['limpa']))
