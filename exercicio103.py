def ficha(nome='SEM NOME',gols=-1):
    print('O Jogado ',end='')
    if gols > -1:
        print(f'{nome} marcou {gols} ',end='')
    else:
        print(f'{nome} marcou INDEFINIDOS ',end='')
    print(' gols')

ficha('Daniel',5)
ficha(gols=5)
ficha('Jose')