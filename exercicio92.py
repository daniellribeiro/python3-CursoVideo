import datetime
pessoa = {}
pessoa['nome'] = input('Digite o seu nome: ')
pessoa['anoNascimento'] = int(input('Em que ano vc nasceu: '))
pessoa['carteiraTrabalho'] = input('Digite sua Carteira Trabalho  0 - NAO POSSUI: ')

pessoa['idade'] = datetime.datetime.now().year - pessoa['anoNascimento']
if pessoa['carteiraTrabalho'] != '0':
    pessoa['anoContratacao'] = int(input('Em que ano vc foi contratado: '))
    pessoa['salario'] = int(input('Digite o valor do seu salario: R$'))
    pessoa['anoAposentadoria'] = pessoa['anoContratacao'] + 35
    pessoa['idadeAposentadoria'] = pessoa['anoAposentadoria'] - pessoa['anoNascimento']

for i,v in pessoa.items():
    print(f'{i}: {v}')
