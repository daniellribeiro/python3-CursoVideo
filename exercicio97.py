texto = ''
def escreva(texto):
        print('~' * (len(texto) + 2))

texto = input('Digite um texto: ')
escreva(texto)
print(f' {texto} ')
escreva(texto)