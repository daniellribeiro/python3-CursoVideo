from metodoCores import corMetodo

funcoes = {
    'inicia': '\033[',
    'limpa': '\033[0m',
    'finaliza': 'm'
}

salario = float(input('Digite o seu salario: '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

cor = (funcoes['inicia'] +
       corMetodo('sublinhado','vermelho','branco') +
       funcoes['finaliza'])

print('Seu aumento sera de R${}, seu salario passara a ser R${}'.format(cor +
                                                                        str(round(aumento,2))
                                                                        + funcoes['limpa'],
                                                                        cor +
                                                                        str(round(salario + aumento,2)) +
                                                                        funcoes['limpa']))
