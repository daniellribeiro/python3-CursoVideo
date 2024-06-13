#Validar um financiamento de uma casa que nao comprometa mais que 30% da renda

import metodoCores

funcoes = {
    'inicia': '\033[',
    'limpa': '\033[0m',
    'finaliza': 'm'
}

valorImovel = float(input('Digite o valor do imovel: '))

salario = float(input('Digite o seu salario: '))

mesesFinanciamento = int(input('Financiara em quantos anos: ')) * 12

parcelaMensal = valorImovel / mesesFinanciamento

valorMaximoPermitido = salario * 0.3

porcRendaComprometida = (parcelaMensal / salario) * 100

corAprovado = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','verde','preto') +
       funcoes['finaliza'])

corNegado = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','vermelho','preto') +
       funcoes['finaliza'])

if(parcelaMensal <= valorMaximoPermitido):
    print('Financiamento {} aprovado!!! {}'.format(corAprovado,funcoes['limpa']))
else:
    print('Financiamento {} negado!!!!! {}'.format(corNegado,funcoes['limpa']))

print('Esse financiamento compromete {:.2f}% do seu salario, e o valor da parcela sera {:.2f}'.format(porcRendaComprometida, parcelaMensal))
