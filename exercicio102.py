def fatorial(numero, exibirTela=False):
    """
    FUNCAO CALCULAR FATORIAL
    :param numero:
    :param exibirTela:
    :return: RESULTADO
    """
    retorno = numero
    while numero > 1:
        numero -= 1
        if exibirTela:
            print(f'{retorno} * {numero} = {retorno * numero}')
        retorno = retorno * numero

    return f'RESULTADO: {retorno}'

print(fatorial(5,True))
#help(fatorial)