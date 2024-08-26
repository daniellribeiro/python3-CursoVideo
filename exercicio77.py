palavras = ('bicicleta','armario','cama','carro','urso')
vogais = []
for palavra in palavras:
    vogais = []
    print(f'{palavra} ==>> ',end=' ')
    for letra in palavra:
        if letra.upper() in ('AEIOU'):
            vogais.append(letra)
    print(f'{sorted(set(vogais))}\n')