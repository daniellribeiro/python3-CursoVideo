#Validar se essa frase e um palindromo

palavraDigitada = input('Digite uma frase: ')

palavra = palavraDigitada.upper().replace(" ","")

palavraInvertida = palavra[::-1]

if(palavra == palavraInvertida):
    print('E um palindromo')
else:
    print('Nao e um palindromo')