
pessoas = []
somatorioIdade = 0
nomeMulheres = []
pessoaIdadeMaiorMedia = []
media = 0

while True:
    pessoa = {
        'nome': input('Digite seu nome: '),
        'sexo': input('Digite seu sexo F-Feminino/M-Masculino: '),
        'idade': int(input('Digite sua idade: '))
    }

    pessoas.append(pessoa)
    somatorioIdade += pessoa['idade']

    if input('Deseja continuar N - NAO S - SIM: ') in 'Nn':
        break

print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
media = round(somatorioIdade / len(pessoas),2)

for i in pessoas:
    if i['sexo'] in 'Ff':
        nomeMulheres.append(i['nome'])
    if i['idade'] > media:
        pessoaIdadeMaiorMedia.append(i)

print(f'A media de idade e {media}')

print(f'As mulheres cadastradas sao: {nomeMulheres}')

print(f'A media de idade e {media}, e essas pessoas possuem idade acima da media: ')
print(pessoaIdadeMaiorMedia)