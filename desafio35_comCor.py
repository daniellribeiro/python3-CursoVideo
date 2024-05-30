import metodoCores

funcoes = {
    'inicia': '\033[',
    'limpa': '\033[0m',
    'finaliza': 'm'
}

lado1 = float(input('Digite o comprimento do 1 lado do triangulo: '))
lado2 = float(input('Digite o comprimento do 2 lado do triangulo: '))
lado3 = float(input('Digite o comprimento do 3 lado do triangulo: '))

isPossivel = lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2

cor = (funcoes['inicia'] +
       metodoCores.corMetodo('nenhum','azul','amarelo') +
       funcoes['finaliza'])
print('{}{}{} possivel formar um triangulo com os comprimentos {},{},{}'.format(cor,
                                                                                'E' if isPossivel
                                                                                    else 'Nao e',
                                                                                funcoes['limpa'],
                                                                                lado1,
                                                                                lado2,
                                                                                lado3))