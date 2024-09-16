pessoas = []
nomesMaiorPeso = []
nomesMenorPeso = []
maiorPeso = menorPeso = 0

while True:
    pessoa = []
    pessoa.append(input('Digite seu nome: '))
    pessoa.append(int(input('Digite seu peso: ')))
    pessoas.append(pessoa)
    if len(pessoas) == 1:
        maiorPeso = menorPeso = pessoa[1]
    if maiorPeso < pessoa[1]:
        maiorPeso = pessoa[1]
    if menorPeso > pessoa[1]:
        menorPeso = pessoa[1]

    if int(input('Deseja continuar ? 1 - SIM 0 - NAO: ')) == 0:
        break

print(f'Voce cadastrou {len(pessoas)} pessoas')

for nome, peso in pessoas:
    if peso == maiorPeso:
        nomesMaiorPeso.append(nome)
    if peso == menorPeso:
        nomesMenorPeso.append(nome)

print(f'O maior peso e {maiorPeso}, as pessoas que possuem esse peso sao {nomesMaiorPeso}')
print(f'O menor peso e {menorPeso}, as pessoas que possuem esse peso sao {nomesMenorPeso}')