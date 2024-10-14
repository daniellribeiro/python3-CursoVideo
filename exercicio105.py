def notas(notas,sit=False):
    """
    Funcao para analisar notas e situacoes de varios alunos
    :param notas:
    :param sit:
    :return:
    """
    print(f'Foram recebidas {len(notas)} notas')
    print(f'A maior nota foi {max(notas)}')
    print(f'A menor nota foi {min(notas)}')
    media = round(sum(notas) / len(notas),1)
    print(f'A media da turma e {media}')
    if sit:
        if media > 6:
            print('SITUACAO BOA')
        else:
            print('SITUACAO RUIM')

notas([5.5,9.5,10,6.5],sit=True)
help(notas)