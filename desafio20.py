#Ler o nome de 4 alunos, e sortear uma ordem

import random

quantidadeAlunos = int(input('Quantos alunos participaram do sorteio: '))
alunos = []
for i in range(quantidadeAlunos):
    alunos.append(input('Digite o nome do aluno n {}: '.format(i + 1)))

random.shuffle(alunos)

for i in range(quantidadeAlunos):
    print('A ordem e {} => {}'.format(i + 1,alunos[i]))


