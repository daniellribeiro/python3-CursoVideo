def validarNumerico():
    n = input('Digite um valor:')
    try:
        return float(n.replace(',','.'))
    except:
        print(f'{n} NAO E UM NUMERO VALIDO')
        exit()

def arredondarEVirgula(n):
    valor = str(n)
    return valor.replace('.',',')