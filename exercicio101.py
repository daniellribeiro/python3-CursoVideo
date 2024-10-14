from datetime import datetime
from datetime import date

def voto(anoNascimento):
    idade = int(datetime.now().strftime("%Y")) - int(anoNascimento)
    if idade >= 18 and idade <= 65:
        opcao = 'OBRIGATORIO'
    elif idade < 16:
        opcao = 'NEGADO'
    else:
        opcao = 'OPCIONAL'
    return f'VOTO {opcao} - COM {idade} anos'

print(voto(input('Ano Nascimento: ')))