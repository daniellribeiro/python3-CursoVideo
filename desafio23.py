numeroLista = list(input('Digite um numero: '))
classe = ['      ','milhar','milhao','bilhao']
ordem = ['unidade','dezena','centena']
contadorOrdem = 0
contadorClasse = 0

for numero in numeroLista[::-1]:
    print('{} {}: {}'.format(classe[contadorClasse],ordem[contadorOrdem],numero))
    contadorOrdem += 1

    if contadorOrdem == len(ordem):
        contadorClasse += 1
        contadorOrdem = 0