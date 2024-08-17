from random import randint

numeroComputador = numeroUsuario = soma = contador = 0
usuarioEscolheu = resultado = ''

while True:
    numeroComputador = randint(0,10)
    numeroUsuario = int(input('Digite um numero de 0 a 10: '))
    usuarioEscolheu = input('Digite I - Impar e P - PAR: ')
    soma = numeroUsuario + numeroComputador
    if soma%2==0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'USUARIO: {numeroUsuario} / PC: {numeroComputador} a soma deu {soma} que e {resultado}')
    if(soma%2==0 and usuarioEscolheu in ('Pp')) or (soma%2!=0 and usuarioEscolheu in ('Ii')):
        print('VOCE VENCEU !!!!')
        contador += 1
    else:
        print('VOCE PERDEU !!!!')
        break

print(f'Voce venceu {contador}')