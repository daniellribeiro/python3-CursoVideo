import metodoCores

funcoes = {
    'inicia':'\033[',
    'limpa':'\033[m'
}
def manual():
    funcao = ''
    cor = metodoCores.corMetodo(estiloEscolha='nenhum',corEscolha='preto',backgroundEscolha='branco')
    while True:
        print('Para encerrar digite Exit')
        funcao = input('Funcao ou Biblioteca: ')
        if funcao.upper() == 'EXIT':
            break
        print('~' * (len(funcao) + 2))
        print(f' {funcao} ')
        print('~' * (len(funcao) + 2))
        print(help(funcao))
manual()