estilo = {
    'nenhum': '0',
    'negrito': '1',
    'sublinado': '4',
    'negativo': '7',
}

text = {
    'preto': '30',
    'vermelho': '31',
    'verde': '32',
    'amarelo': '33',
    'azul': '34',
    'roxo': '35',
    'manjenta': '36',
    'branco': '37'
}

background = {
    'preto': '40',
    'vermelho': '41',
    'verde': '42',
    'amarelo': '43',
    'azul': '44',
    'roxo': '45',
    'majenta': '46',
    'branco': '47'
}

funcoes = {
    'inicia':'\033[',
    'limpa':'\033[m'
}

texto = input('Digite o texto que vc quer colorir: ')
print(estilo)
estiloEscolha = input('Digite o codigo do estilo: ')
estiloEscolha += ';'

print(text)
escolhaCor = input('Digite o codigo da cor do texto: ')
escolhaCor += ';'

print(background)
escolhaBackground = input('Digite o codigo da cor de fundo: ')
escolhaBackground += 'm'


cor = funcoes['inicia'] + estiloEscolha + escolhaCor + escolhaBackground
print('Abaixo seu texto colorido: ')
print('{}{}{}'.format(cor,texto,funcoes['limpa']))



