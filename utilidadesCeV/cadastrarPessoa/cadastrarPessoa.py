import os

nomeArquivo = 'C:/Users/daniel/Documents/pessoas.txt'
def salvarArquivo(nome, idade):
    with open(nomeArquivo, 'a') as arquivo:
        arquivo.write(f'{nome},{idade}\n')
        print('Dados salvos com sucesso!!!')
        arquivo.close()

def lerArquivo():
    aux = {}
    lista = []

    if not os.path.exists(nomeArquivo):
        print('ARQUIVO NAO EXISTE!!!!')
        return lista
    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            aux = {'nome': linha.strip().split(',')[0],
                    'idade': linha.strip().split(',')[1]}
            lista.append(aux)
        arquivo.close()
        return lista
