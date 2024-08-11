from random import randint

numeroComputador = 0
numeroUsuario = 0
soma = 0
usuarioEscolheu = ''
contador = 0

while True:
    numeroComputador = randint(0,10)
    numeroUsuario = int(input('Digite um numero de 0 a 10: '))
    usuarioEscolheu = input('Digite I - Impar e P - PAR: ')
    print(f'USUARIO: {numeroUsuario} / PC: {numeroComputador}')
    soma = numeroUsuario + numeroComputador
    if(soma%2==0 and usuarioEscolheu in ('Pp')) or (soma%2!=0 and usuarioEscolheu in ('Ii')):
        print('VOCE VENCEU !!!!')
        contador += 1
    else:
        print('VOCE PERDEU !!!!')
        break

print(f'Voce venceu {contador}')