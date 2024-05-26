#Ler o nome de 4 alunos, e sortear um

import random

quantidadeAlunos = int(input('Quantos alunos participaram do sorteio: '))
alunos = []
for i in range(quantidadeAlunos):
    alunos.append(input('Digite o nome do aluno n {}: '.format(i + 1)))

print('O aluno sorteado foi {}'.format(random.choice(alunos)))