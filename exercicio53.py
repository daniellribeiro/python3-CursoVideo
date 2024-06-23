#Validar se essa frase e um palindromo

palavraDigitada = input('Digite uma frase: ')

palavra = palavraDigitada.upper().replace(" ","")

palavraInvertida = palavra[::-1]

print('O inverso de {} e {}'.format(palavra,palavraInvertida))
if(palavra == palavraInvertida):
    print('E um palindromo')
else:
    print('Nao e um palindromo')