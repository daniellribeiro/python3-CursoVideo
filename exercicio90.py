aluno = {}

aluno['nome'] = input('Digite o seu nome: ')
aluno['media'] = float(input('Digite a sua media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'RECUPERACAO'
else:
    aluno['situacao'] = 'REPROVADO'
print(aluno.items())
