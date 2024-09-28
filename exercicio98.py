from time import sleep


def contagem(inicio, fim, passo):
    if (inicio > fim and passo > 0) or (inicio < fim and passo < 0):
        passo *= -1
    elif passo == 0 and inicio < fim:
        passo = 1
    elif passo == 0 and inicio > fim:
        passo = -1

    print(f'\nContagem de {inicio} a {fim}, {'aumentando' if passo > 0 else 'diminuindo'} de {abs(passo)} em {abs(passo)}')
    fim = fim + 1 if passo > 0 else fim - 1
    for i in range(inicio, fim, passo):
        print(f' {i} ', end='')
        sleep(0.5)


contagem(1, 10, 1)
contagem(10, 0, -2)
print('\n')
contagem(int(input('Inicio: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))