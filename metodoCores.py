estilo = {
    'nenhum': '0;',
    'negrito': '1;',
    'sublinhado': '4;',
    'negativo': '7;;',
}

text = {
    'preto': '30;',
    'vermelho': '31;',
    'verde': '32;',
    'amarelo': '33;',
    'azul': '34;',
    'roxo': '35;',
    'magenta': '36;',
    'branco': '37;'
}

background = {
    'preto': '40',
    'vermelho': '41',
    'verde': '42',
    'amarelo': '43',
    'azul': '44',
    'roxo': '45',
    'magenta': '46',
    'branco': '47'
}

def corMetodo(estiloEscolha,corEscolha,backgroundEscolha):
    if (estiloEscolha not in estilo) or (corEscolha not in text) or (backgroundEscolha not in background):
        return ''
    return (estilo[estiloEscolha] +
            text[corEscolha] +
            background[backgroundEscolha])
