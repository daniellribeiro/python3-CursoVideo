from time import sleep

def maior(* aux):
    if len(aux) > 0:
        print(f'Analisando valores os {len(aux)} valores passados')
        maiorNumero = aux[0]
        for i in range(len(aux)):
            sleep(0.5)
            print(f' {aux[i]} ',end=' ')
            if maiorNumero < aux[i]:
                maiorNumero = aux[i]
        print('\n')
        return maiorNumero
    else:
        print('nao foi informado nenhum valor')
        return 0


print(f'O maior valor foi {maior(2,9,4,5,7,1)}')

print(f'O maior valor foi {maior(4,7,0)}')

print(f'O maior valor foi {maior(1,2)}')

print(f'O maior valor foi {maior(6)}')

print(f'O maior valor foi {maior()}')
