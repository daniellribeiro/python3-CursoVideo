pessoas = []
somaIdade = 0
maiorIdadeM = 0
menos20F = 0
nomeMaisVelho = ''

for i in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite F - Feminino e M - Masculino: ')
    pessoa = (nome, idade, sexo)
    pessoas.append(pessoa)

for i in pessoas:
    nome,idade,sexo = i

    somaIdade += idade

    if idade > maiorIdadeM and sexo in 'Mm':
        maiorIdadeM = idade
        nomeMaisVelho = nome

    if idade < 20 and sexo in 'Ff':
        menos20F += 1

print('A media de idade e {}'.format(somaIdade / 4))
print('O homem mais velho e o Seu {}, que possui {} anos'.format(nomeMaisVelho,maiorIdadeM))
print('Tem {} mulheres com menos de 20 anos'.format(menos20F))
