from utilidadesCeV.dado.dado import arredondarEVirgula


def metade(n,formatado=False):
    return moeda(n/2,formatado)
def dobro(n,formatado=False):
    n = float(n)
    return moeda(n*2,formatado)
def aumentar(n,p,formatado=False):
    return moeda(n + calcularPorcentagemNumero(n,p),formatado)

def diminuir(n,p,formatado=False):
    return moeda(n - calcularPorcentagemNumero(n,p),formatado)

def calcularPorcentagemNumero(n,p):
    return n * (p / 100)

def moeda(n,formatado=True):
    if formatado:
        n = arredondarEVirgula('{:.2f}'.format(n))
        return f'R$ {n}'
    else:
        return n

def resumo(n=0,aumento=0,reducao=0):
    print('------------------------------------------------')
    print('     RESUMO DO VALOR      ')
    print('------------------------------------------------')
    print(f'Preco analisado: {moeda(n)}')
    print(f'Dobro do preco:  {dobro(n,True)}')
    print(f'Metade do preco: {metade(n,True)}')
    print(f'{aumento}% de aumento:  {aumentar(n,aumento,True)}')
    print(f'{reducao}% de reducao:  {diminuir(n,reducao,True)}')
    print('------------------------------------------------')